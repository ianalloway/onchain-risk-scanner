# On-chain Risk Scanner

Read-only anomaly and risk triage for Ethereum, Base, Optimism, and Arbitrum contracts.

This project is built as public proof-of-work for Web3 security, grant applications, and white-hat research. It does not exploit contracts, send transactions, or require private keys. It fetches runtime bytecode and proxy storage through JSON-RPC, then produces a short report that points reviewers toward security-relevant follow-up questions.

## Why This Exists

Security researchers, grant reviewers, and builders often need a quick first pass on a contract before deeper manual review. This scanner focuses on signals that are useful early:

- EIP-1967 proxy implementation, admin, and beacon slots
- high-impact opcodes such as `DELEGATECALL`, `SELFDESTRUCT`, `CALLCODE`, and `ORIGIN`
- common privileged function selectors such as upgrade, ownership, pause, mint, and withdraw flows
- deterministic risk scoring with readable markdown and JSON output

The goal is not to replace audits. The goal is to turn “where should I look first?” into a repeatable, public, open-source workflow.

## Install

```bash
cd /Users/ianalloway/Documents/Codex/onchain-risk-scanner
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

## Usage

Scan a Base contract with the default public RPC:

```bash
onchain-risk 0x4200000000000000000000000000000000000006 --chain base
```

Run the grant/demo flow:

```bash
./scripts/demo.sh
```

Write a markdown report:

```bash
onchain-risk 0x4200000000000000000000000000000000000006 \
  --chain base \
  --out reports/base-weth.md
```

Use your own RPC endpoint:

```bash
onchain-risk 0x0000000000000000000000000000000000000000 \
  --chain ethereum \
  --rpc-url "$ETH_RPC_URL" \
  --format json
```

## Example Output

See [examples/base-weth.md](examples/base-weth.md) for a real read-only scan of the canonical WETH-style contract on Base.

```markdown
# On-chain Risk Report: `0x...`

- Chain: `base` (8453)
- Risk score: **34/100** (low)
- Runtime bytecode: `12345` bytes

## Findings

### MEDIUM: DELEGATECALL present

Delegatecall can be legitimate for proxies and libraries, but it raises the impact of storage-layout and implementation-control bugs.
```

## Current Heuristics

| Area | Signal | Why it matters |
| --- | --- | --- |
| Proxy metadata | EIP-1967 implementation/admin/beacon slots | Upgrade rights can dominate real protocol risk. |
| Runtime bytecode | size and opcode profile | Large or unusual contracts need deeper review. |
| Dangerous opcodes | `DELEGATECALL`, `SELFDESTRUCT`, `CALLCODE`, `ORIGIN` | These can create upgrade, availability, legacy, or auth risks. |
| Privileged selectors | upgrade, owner, pause, mint, withdraw | These are not automatically bugs, but they define the human review map. |

## Roadmap

- Add verified-source ingestion from Etherscan-compatible APIs.
- Add event and transaction anomaly modules for TVL movement, admin actions, and upgrade history.
- Add protocol-specific profiles for ERC-20, vaults, bridges, and lending markets.
- Add SARIF output for GitHub code-scanning style workflows.
- Publish weekly white-hat notes that explain one real contract pattern at a time without disclosing exploitable details.

## Grant Fit

This is intentionally scoped as an open-source public good:

- **Base Builder Grants:** scan and document Base contracts, publish reports, and add Base-specific risk profiles.
- **Optimism Grants / Retro Funding:** build dev tooling that helps Superchain users and builders identify upgrade/admin risk.
- **Ethereum ESP:** extend static and on-chain analysis for Ethereum public goods, wallet safety, and security education.
- **Gitcoin Grants:** fund open-source security tooling, public reports, and educational writeups.

See [docs/grant-strategy.md](docs/grant-strategy.md) for the first funding plan.

## White-hat Safety

This project is for authorized, read-only analysis. Do not use it to probe out-of-scope systems, attack live protocols, move funds, or bypass access controls. For paid bug bounty work, always read the target program scope and disclosure rules first.

See [docs/whitehat-playbook.md](docs/whitehat-playbook.md).

## Development

```bash
python -m pytest
```

## License

MIT
