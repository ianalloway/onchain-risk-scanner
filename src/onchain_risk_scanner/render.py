from __future__ import annotations

from .scanner import ScanReport


def render_markdown(report: ScanReport) -> str:
    lines = [
        f"# On-chain Risk Report: `{report.address}`",
        "",
        f"- Chain: `{report.chain}` ({report.chain_id})",
        f"- Explorer: {report.explorer_url}",
        f"- Risk score: **{report.risk_score}/100** ({report.risk_band})",
        f"- Runtime bytecode: `{report.bytecode_bytes}` bytes",
        f"- Native balance: `{report.balance_eth}` ETH",
        "",
        "## Proxy",
        "",
    ]
    if report.proxy.detected:
        lines.extend(
            [
                f"- Implementation: `{report.proxy.implementation or 'not detected'}`",
                f"- Admin: `{report.proxy.admin or 'not detected'}`",
                f"- Beacon: `{report.proxy.beacon or 'not detected'}`",
            ]
        )
    else:
        lines.append("- No EIP-1967 proxy metadata detected.")

    lines.extend(["", "## Findings", ""])
    if report.findings:
        for finding in report.findings:
            lines.extend(
                [
                    f"### {finding.severity.upper()}: {finding.title}",
                    "",
                    finding.detail,
                    "",
                ]
            )
    else:
        lines.append("No heuristic findings were raised.")

    lines.extend(["", "## Opcode Hits", ""])
    for name, count in sorted(report.opcode_hits.items()):
        lines.append(f"- `{name}`: {count}")

    lines.extend(["", "## Selector Hits", ""])
    if report.selector_hits:
        for selector, signature in sorted(report.selector_hits.items()):
            lines.append(f"- `0x{selector}`: `{signature}`")
    else:
        lines.append("- No tracked selectors detected.")

    lines.extend(["", "## Notes", ""])
    for note in report.notes:
        lines.append(f"- {note}")

    return "\n".join(lines) + "\n"
