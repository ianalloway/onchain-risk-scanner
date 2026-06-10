from __future__ import annotations

from dataclasses import asdict, dataclass

from .chains import Chain
from .heuristics import (
    EIP1967_ADMIN_SLOT,
    EIP1967_BEACON_SLOT,
    EIP1967_IMPLEMENTATION_SLOT,
    Finding,
    analyze_bytecode,
    extract_address_from_storage,
    risk_band,
)
from .rpc import JsonRpcClient


@dataclass
class ProxyInfo:
    implementation: str | None
    admin: str | None
    beacon: str | None

    @property
    def detected(self) -> bool:
        return bool(self.implementation or self.admin or self.beacon)


@dataclass
class ScanReport:
    chain: str
    chain_id: int
    address: str
    explorer_url: str
    bytecode_bytes: int
    balance_eth: float
    proxy: ProxyInfo
    opcode_hits: dict[str, int]
    selector_hits: dict[str, str]
    findings: list[Finding]
    risk_score: int
    risk_band: str
    notes: list[str]

    def to_dict(self) -> dict:
        result = asdict(self)
        result["proxy"]["detected"] = self.proxy.detected
        return result


def scan_contract(
    *,
    address: str,
    chain: Chain,
    rpc_url: str,
    block: str = "latest",
) -> ScanReport:
    client = JsonRpcClient(rpc_url)
    bytecode = client.get_code(address, block)
    balance_wei = client.get_balance(address, block)
    bytecode_analysis = analyze_bytecode(bytecode)

    implementation = extract_address_from_storage(
        client.get_storage_at(address, EIP1967_IMPLEMENTATION_SLOT, block)
    )
    admin = extract_address_from_storage(
        client.get_storage_at(address, EIP1967_ADMIN_SLOT, block)
    )
    beacon = extract_address_from_storage(
        client.get_storage_at(address, EIP1967_BEACON_SLOT, block)
    )
    proxy = ProxyInfo(implementation=implementation, admin=admin, beacon=beacon)

    findings = list(bytecode_analysis.findings)
    if proxy.detected:
        findings.append(
            Finding(
                severity="medium",
                title="EIP-1967 proxy storage detected",
                detail=(
                    "Proxy metadata was found. Review admin controls, implementation "
                    "history, initialization, and upgrade process before trusting assets."
                ),
                weight=16,
            )
        )

    score = min(100, sum(finding.weight for finding in findings))
    notes = [
        "This scanner is read-only and does not prove exploitability.",
        "Treat findings as triage leads for manual review, not final audit results.",
    ]

    return ScanReport(
        chain=chain.name,
        chain_id=chain.chain_id,
        address=address,
        explorer_url=chain.explorer + address,
        bytecode_bytes=bytecode_analysis.bytecode_bytes,
        balance_eth=round(balance_wei / 10**18, 8),
        proxy=proxy,
        opcode_hits=bytecode_analysis.opcode_hits,
        selector_hits=bytecode_analysis.selector_hits,
        findings=findings,
        risk_score=score,
        risk_band=risk_band(score),
        notes=notes,
    )
