# Grant Strategy

This project should be positioned as open-source security infrastructure for safer on-chain participation.

## Primary Narrative

On-chain users and builders need fast, readable contract risk triage before they interact with unfamiliar protocols. On-chain Risk Scanner makes proxy controls, privileged selectors, and high-risk bytecode patterns visible without requiring private keys or transaction simulation. The tool is useful for developers, wallets, researchers, and public-goods educators.

## First 30 Days

1. Publish the MVP on GitHub with clear install and scan examples.
2. Run 20 public scans across Base and Ethereum contracts.
3. Turn 5 scans into educational writeups focused on safe, non-exploitative lessons.
4. Add verified-source ingestion for Etherscan-compatible APIs.
5. Create a public issue board with grant-sized milestones.

## Best-Fit Programs

| Program | Fit | Ask |
| --- | --- | --- |
| Base Builder Grants | Retroactive funding for shipped Base tooling | 1-5 ETH after Base scans and reports are published. |
| Optimism Grants / Retro Funding | Security/dev tooling for Superchain contracts | Funding for Optimism profile support and public reports. |
| Ethereum ESP | Public-goods security tooling and education | Milestone grant for source ingestion, research notes, and broader Ethereum reports. |
| Gitcoin Grants | Community funding for open-source public goods | Recurring support for reports, docs, and maintenance. |

## Proof Points To Build

- GitHub repo with tests, examples, issues, and roadmap.
- Public markdown reports under `reports/`.
- Short research notes under `research/`.
- Before/after examples showing how a scan guided manual review.
- A “no private keys, no transactions, read-only” safety statement.

## Milestone Proposal

### Milestone 1: Static Contract Risk Triage

- CLI scans Ethereum/Base/Optimism/Arbitrum.
- Proxy metadata detection.
- Opcode and selector heuristics.
- Markdown and JSON output.

### Milestone 2: Source-Aware Analysis

- Pull verified ABI/source metadata from Etherscan-compatible APIs.
- Map selectors to source names.
- Flag owner/admin modifiers where available.

### Milestone 3: On-chain Anomaly Timeline

- Track upgrades, admin changes, token balance shifts, and high-value calls.
- Add repeatable report templates for public research.

### Milestone 4: Public-Goods Reports

- Publish weekly contract-risk notes.
- Create beginner-friendly walkthroughs for reading proxy/admin risk.
- Submit to Gitcoin and ecosystem grant rounds.
