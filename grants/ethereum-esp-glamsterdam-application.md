# Ethereum ESP Glamsterdam Grants Round Application Draft

Application page: https://esp.ethereum.foundation/applicants/wishlist/glamsterdam-round/apply

Public repo: https://github.com/ianalloway/onchain-risk-scanner

## Fit

Ethereum ESP is seeking open-source proposals for Glamsterdam readiness, including developer tooling updates, impact-analysis tooling, explorer/indexer support, monitoring tooling, and data-driven research. This project should be framed as **Glamsterdam Contract Impact Scanner**, an extension of On-chain Risk Scanner focused on identifying contracts likely to be affected by gas repricing, EVM changes, max contract size changes, native ETH transfer logs, and Block-Level Access Lists.

## Contact Information

### First name

Ian

### Last name

Alloway

### Email

`[IAN EMAIL]`

### Company

N/A

### Profile Type

Individual developer / independent researcher

### Alternative Contact Info

GitHub: https://github.com/ianalloway

### Website

https://ianalloway.xyz

### Country

United States

### Time Zone

America/New_York

## Applicant Profile

Ian Alloway is an ML/data-science focused developer building public, open-source tools at the intersection of security, analytics, and developer education. His current project, On-chain Risk Scanner, is a read-only contract triage CLI for Ethereum, Base, Optimism, and Arbitrum. It produces Markdown and JSON reports from JSON-RPC data without private keys or transactions, making it suitable for public-good security education and non-invasive ecosystem analysis.

## Budget

### Budget Request

USD 18,000

### Currency

USD

Budget rationale: 10 weeks of implementation, analysis, documentation, and public reporting. The scope is intentionally modest and milestone-based.

## Project Overview

### Project Name

Glamsterdam Contract Impact Scanner

### Project Summary

Glamsterdam Contract Impact Scanner will extend On-chain Risk Scanner into an open-source impact-analysis tool for the upcoming Ethereum Glamsterdam upgrade. The project will help developers and researchers identify contracts that may deserve manual review because of runtime bytecode size, opcode usage, upgrade/proxy design, native ETH movement patterns, and other signals relevant to proposed Glamsterdam changes. The output will be reproducible Markdown/JSON reports and a public research note set.

Existing public work:

- Repo: https://github.com/ianalloway/onchain-risk-scanner
- Example Base report: https://github.com/ianalloway/onchain-risk-scanner/blob/main/examples/base-weth.md

### Project Repo Link

https://github.com/ianalloway/onchain-risk-scanner

### Domain

Ethereum Protocol / Developer tooling / Impact analysis tooling

### Output

Open-source software, documentation, and public research reports

## Project Details

### Project Structure

**Milestone 1: Glamsterdam readiness mapping, week 1**

- Review EIP-7773, Forkcast Glamsterdam status, and relevant All Core Devs notes.
- Create a public mapping from likely Glamsterdam changes to scanner signals.
- Publish `docs/glamsterdam-impact-model.md`.

**Milestone 2: Impact-analysis modules, weeks 2-5**

- Add verified source and ABI ingestion for Etherscan-compatible APIs.
- Add contract-size, opcode, proxy, and selector modules aligned to Glamsterdam impact questions.
- Add JSON schema for downstream analysis and reproducible reports.

**Milestone 3: Ethereum mainnet scan set, weeks 6-8**

- Run and publish a curated set of read-only reports for Ethereum public contracts.
- Focus on safe, educational findings and avoid exploit disclosure.
- Document methodology, limitations, and false-positive controls.

**Milestone 4: Public release and research notes, weeks 9-10**

- Release v0.2.0.
- Publish 3-5 research notes explaining upgrade-readiness patterns.
- Create contribution guidelines for additional ecosystem maintainers.

### Sustainability Plan

The project will remain MIT-licensed and open source. After the grant, sustainability will come from Gitcoin public-goods rounds, Base/OP retroactive grants for L2-specific impact, GitHub Sponsors, and public consulting/audit-prep work that does not compromise the open-source core. The scanner is designed to stay low-cost: it runs locally, depends on JSON-RPC and optional explorer APIs, and can be maintained with small milestone grants.

### Funding

No confirmed funding at the time of this draft. Base Builder Grants and Gitcoin public-goods funding are being pursued as complementary, non-overlapping support for L2-specific reports and community maintenance.

### Problem Being Solved

Major Ethereum upgrades can change the risk profile of deployed contracts, tooling, and monitoring systems. Builders need a practical way to identify which contracts deserve human review before and after a network upgrade. Today, much of this review is manual, scattered across explorers, repos, and private notes. This project provides a reproducible, open-source triage layer that turns upgrade-readiness questions into concrete contract reports.

Concrete examples:

- Contracts near size limits may be relevant if max contract size changes.
- Contracts with unusual opcode usage may deserve review as EVM capabilities and gas pricing evolve.
- Proxy-admin and upgradeable systems need clear visibility before integration decisions.
- Public researchers need safe reports that educate without publishing exploit instructions.

### Measured Impact

Current project status:

- Public GitHub repository is live.
- CLI supports Ethereum, Base, Optimism, and Arbitrum.
- Test suite and GitHub Actions workflow are included.
- A real Base mainnet scan report has been published as an example.
- Public roadmap issues are open for source ingestion, upgrade/admin timelines, Base reports, and bounty-safe reproduction.

### Success Metrics

- v0.2.0 released within 10 weeks.
- At least 30 Ethereum mainnet contracts scanned with reproducible reports.
- At least 3 public research notes published.
- Verified-source ingestion implemented for Etherscan-compatible APIs.
- JSON report schema documented and used by all published reports.
- At least 5 external users, issues, stars, forks, comments, or community feedback events recorded.

### Ecosystem Fit

Similar ecosystem tools include Etherscan, Sourcify, Slither, Foundry, Tenderly, and block explorers. On-chain Risk Scanner is different because it is lightweight, read-only, chain-RPC-first, report-oriented, and focused on public upgrade-readiness and risk triage rather than full static analysis or transaction simulation. It complements Slither and Foundry by helping researchers decide where to look first, then handing off to deeper tools for source-level or fork-test validation.

### Community Feedback

Current feedback is early. The project has been published publicly and seeded with roadmap issues to invite review. The next step is to share the Base scan example with Base, Ethereum, and Web3 security communities and collect comments from developers/security researchers before finalizing v0.2.0 modules.

### Open Source License

MIT

## Additional Details

### Have you applied before to any grants at the Ethereum Foundation?

No

### Referral(s)

No referral yet.

### Additional questions or comments

The project is deliberately read-only and avoids exploit execution. Reports are framed as triage and education, not vulnerability disclosure. If selected, I would welcome ESP feedback on the most useful Glamsterdam signals to prioritize.

### Allow contact from Ethereum Foundation about other opportunities?

Yes
