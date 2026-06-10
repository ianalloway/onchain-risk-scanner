from onchain_risk_scanner.heuristics import Finding
from onchain_risk_scanner.render import render_markdown
from onchain_risk_scanner.scanner import ProxyInfo, ScanReport


def test_render_markdown_includes_risk_and_findings() -> None:
    report = ScanReport(
        chain="base",
        chain_id=8453,
        address="0x0000000000000000000000000000000000000000",
        explorer_url="https://basescan.org/address/0x0",
        bytecode_bytes=128,
        balance_eth=0.0,
        proxy=ProxyInfo(implementation=None, admin=None, beacon=None),
        opcode_hits={"delegatecall": 0},
        selector_hits={},
        findings=[
            Finding(
                severity="low",
                title="Example",
                detail="Example detail.",
                weight=1,
            )
        ],
        risk_score=1,
        risk_band="info",
        notes=["Read-only."],
    )

    output = render_markdown(report)

    assert "# On-chain Risk Report" in output
    assert "Risk score: **1/100**" in output
    assert "LOW: Example" in output
