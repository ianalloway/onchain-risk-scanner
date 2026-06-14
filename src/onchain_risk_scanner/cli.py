from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from .chains import CHAINS, get_chain
from .render import render_markdown
from .rpc import RpcError
from .scanner import scan_contract
from .timeline import render_timeline_markdown, scan_timeline


ADDRESS_PATTERN = re.compile(r"^0x[a-fA-F0-9]{40}$")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="onchain-risk",
        description="Read-only risk scanner for Ethereum, Base, Optimism, and Arbitrum contracts.",
    )
    subparsers = parser.add_subparsers(dest="command")

    scan_parser = subparsers.add_parser("scan", help="Run bytecode, proxy, and selector triage.")
    add_common_args(scan_parser)
    scan_parser.add_argument("--block", default="latest", help="Block tag or hex block number.")
    scan_parser.add_argument(
        "--format",
        choices=["markdown", "json"],
        default="markdown",
        help="Output format.",
    )
    scan_parser.add_argument("--out", help="Write report to this path instead of stdout.")

    timeline_parser = subparsers.add_parser(
        "timeline",
        help="Build an upgrade/admin event timeline for a contract.",
    )
    add_common_args(timeline_parser)
    timeline_parser.add_argument("--from-block", type=int, help="Start block. Defaults to latest - 1000.")
    timeline_parser.add_argument("--to-block", type=int, help="End block. Defaults to latest.")
    timeline_parser.add_argument(
        "--format",
        choices=["markdown", "json"],
        default="markdown",
        help="Output format.",
    )
    timeline_parser.add_argument("--out", help="Write report to this path instead of stdout.")
    return parser


def add_common_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("address", help="Contract address to scan.")
    parser.add_argument(
        "--chain",
        default="base",
        choices=sorted(CHAINS),
        help="Chain to scan. Defaults to base.",
    )
    parser.add_argument(
        "--rpc-url",
        help="JSON-RPC URL. Defaults to a public RPC for the selected chain.",
    )


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    raw_args = list(argv if argv is not None else sys.argv[1:])
    commands = {"scan", "timeline"}
    if raw_args and raw_args[0] not in commands and not raw_args[0].startswith("-"):
        raw_args.insert(0, "scan")
    args = parser.parse_args(raw_args)

    if not ADDRESS_PATTERN.match(args.address):
        parser.error("address must be a 20-byte hex address, e.g. 0x1234...")

    chain = get_chain(args.chain)
    rpc_url = args.rpc_url or chain.public_rpc
    if not rpc_url:
        parser.error(f"No default RPC configured for {chain.name}; pass --rpc-url.")

    try:
        if args.command == "timeline":
            report = scan_timeline(
                address=args.address,
                chain=chain,
                rpc_url=rpc_url,
                from_block=args.from_block,
                to_block=args.to_block,
            )
        else:
            report = scan_contract(
                address=args.address,
                chain=chain,
                rpc_url=rpc_url,
                block=args.block,
            )
    except (RpcError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if args.format == "json":
        output = json.dumps(report.to_dict(), indent=2, sort_keys=True) + "\n"
    elif args.command == "timeline":
        output = render_timeline_markdown(report)
    else:
        output = render_markdown(report)

    if args.out:
        Path(args.out).write_text(output, encoding="utf-8")
    else:
        print(output, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
