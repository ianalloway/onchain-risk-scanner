from __future__ import annotations

from dataclasses import dataclass, field


EIP1967_IMPLEMENTATION_SLOT = (
    "0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc"
)
EIP1967_ADMIN_SLOT = (
    "0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103"
)
EIP1967_BEACON_SLOT = (
    "0xa3f0ad74e5423aebfd80d3ef4346578335a9a72aeaee59ff6cb3582b35133d50"
)

OPCODES = {
    "delegatecall": 0xF4,
    "selfdestruct": 0xFF,
    "callcode": 0xF2,
    "origin": 0x32,
}

SELECTORS = {
    "3659cfe6": "upgradeTo(address)",
    "4f1ef286": "upgradeToAndCall(address,bytes)",
    "79ba5097": "acceptOwnership()",
    "f2fde38b": "transferOwnership(address)",
    "8456cb59": "pause()",
    "3f4ba83a": "unpause()",
    "40c10f19": "mint(address,uint256)",
    "a9059cbb": "transfer(address,uint256)",
    "23b872dd": "transferFrom(address,address,uint256)",
    "2e1a7d4d": "withdraw(uint256)",
    "3ccfd60b": "withdraw()",
    "715018a6": "renounceOwnership()",
    "8f283970": "changeAdmin(address)",
}


@dataclass(frozen=True)
class Finding:
    severity: str
    title: str
    detail: str
    weight: int


@dataclass
class BytecodeAnalysis:
    bytecode_bytes: int
    opcode_hits: dict[str, int] = field(default_factory=dict)
    selector_hits: dict[str, str] = field(default_factory=dict)
    findings: list[Finding] = field(default_factory=list)


def normalize_hex(value: str) -> str:
    if not value:
        return ""
    return value[2:].lower() if value.startswith("0x") else value.lower()


def extract_address_from_storage(value: str) -> str | None:
    raw = normalize_hex(value).rjust(64, "0")
    if int(raw, 16) == 0:
        return None
    return "0x" + raw[-40:]


def count_opcodes(raw_hex: str) -> dict[str, int]:
    code = bytes.fromhex(raw_hex) if raw_hex else b""
    counts = dict.fromkeys(OPCODES, 0)
    position = 0
    while position < len(code):
        opcode = code[position]
        for name, target in OPCODES.items():
            if opcode == target:
                counts[name] += 1
        if 0x60 <= opcode <= 0x7F:
            position += 1 + (opcode - 0x5F)
        else:
            position += 1
    return counts


def analyze_bytecode(bytecode: str) -> BytecodeAnalysis:
    raw = normalize_hex(bytecode)
    analysis = BytecodeAnalysis(bytecode_bytes=len(raw) // 2)

    analysis.opcode_hits = count_opcodes(raw)

    for selector, signature in SELECTORS.items():
        if selector in raw:
            analysis.selector_hits[selector] = signature

    if not raw:
        analysis.findings.append(
            Finding(
                severity="info",
                title="No contract bytecode",
                detail="The address has no deployed runtime bytecode at the selected block.",
                weight=0,
            )
        )
        return analysis

    if analysis.bytecode_bytes > 24_000:
        analysis.findings.append(
            Finding(
                severity="medium",
                title="Large contract bytecode",
                detail=(
                    "Runtime bytecode is close to or above the common EVM contract "
                    "size limit, which can make review and upgrade safety harder."
                ),
                weight=10,
            )
        )

    if analysis.opcode_hits["delegatecall"]:
        analysis.findings.append(
            Finding(
                severity="medium",
                title="DELEGATECALL present",
                detail=(
                    "Delegatecall can be legitimate for proxies and libraries, but it "
                    "raises the impact of storage-layout and implementation-control bugs."
                ),
                weight=18,
            )
        )

    if analysis.opcode_hits["selfdestruct"]:
        analysis.findings.append(
            Finding(
                severity="high",
                title="SELFDESTRUCT present",
                detail="Selfdestruct behavior can create availability and asset-safety risks.",
                weight=22,
            )
        )

    if analysis.opcode_hits["callcode"]:
        analysis.findings.append(
            Finding(
                severity="high",
                title="CALLCODE present",
                detail="CALLCODE is legacy behavior and often signals unusual execution risk.",
                weight=18,
            )
        )

    if analysis.opcode_hits["origin"]:
        analysis.findings.append(
            Finding(
                severity="low",
                title="ORIGIN opcode present",
                detail="tx.origin usage can be unsafe for authorization if used directly.",
                weight=8,
            )
        )

    privileged = [
        signature
        for signature in analysis.selector_hits.values()
        if signature
        in {
            "upgradeTo(address)",
            "upgradeToAndCall(address,bytes)",
            "changeAdmin(address)",
            "mint(address,uint256)",
            "pause()",
            "unpause()",
            "transferOwnership(address)",
            "renounceOwnership()",
        }
    ]
    if privileged:
        analysis.findings.append(
            Finding(
                severity="low",
                title="Privileged selectors detected",
                detail=(
                    "Potential privileged entrypoints found in bytecode: "
                    + ", ".join(sorted(privileged))
                ),
                weight=min(18, 4 * len(privileged)),
            )
        )

    return analysis


def risk_band(score: int) -> str:
    if score >= 70:
        return "high"
    if score >= 35:
        return "medium"
    if score >= 12:
        return "low"
    return "info"
