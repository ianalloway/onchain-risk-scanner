# Gitcoin GG24 / Public-Goods Profile Draft

Gitcoin page: https://grants.gitcoin.co/

Best current domains to evaluate:

- Developer Tooling & Infrastructure
- Interop Standards, Infra and Analytics
- Public Goods Tooling Development, if open and eligible

## Project Name

On-chain Risk Scanner

## One-Liner

Read-only contract risk triage for Ethereum and L2 builders.

## Short Description

On-chain Risk Scanner is an open-source CLI that scans Ethereum, Base, Optimism, and Arbitrum contracts through JSON-RPC and produces readable Markdown/JSON risk reports. It helps builders and researchers quickly identify proxy metadata, privileged selectors, and opcode-level signals before deeper manual review.

## Long Description

Smart contract security work often starts with a messy question: where should I look first? On-chain Risk Scanner answers that with a simple, reproducible, read-only workflow. It does not need private keys, does not send transactions, and does not attempt exploitation. Instead, it fetches public chain data and turns it into reports that developers, researchers, and grant reviewers can inspect.

The first MVP supports Ethereum, Base, Optimism, and Arbitrum. The next milestones add verified-source ingestion, upgrade/admin timelines, protocol-specific risk profiles, and public research notes. Funding will support open-source security tooling and educational reporting for public-good infrastructure.

## Impact

- Makes contract-risk triage easier for builders and early security learners.
- Produces public reports that can be reused in research and education.
- Helps L2 ecosystems understand upgrade/admin risk in deployed contracts.
- Creates a bridge from ML/data analysis work into Web3 security tooling.

## Funding Goal

USD 8,000-15,000 equivalent.

## Use of Funds

- Verified-source ingestion for Etherscan-compatible APIs.
- Public scan sets for Base, Ethereum, and Optimism.
- Upgrade/admin event timeline module.
- Documentation and beginner-friendly white-hat research notes.
- Maintenance, issue triage, and community onboarding.

## Links

- GitHub: https://github.com/ianalloway/onchain-risk-scanner
- Website: https://ianalloway.xyz
- Example report: https://github.com/ianalloway/onchain-risk-scanner/blob/main/examples/base-weth.md

## Wallet

`0x6F278Ce76BA5ED31Fd9bE646D074863e126836E9`

Do not paste a seed phrase or private key. Only use a public address.
