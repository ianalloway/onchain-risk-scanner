# Base Builder Grants Nomination

Application page: https://docs.google.com/forms/d/e/1FAIpQLSfXuEzmiAzRhie_z9raFCF1BXweXgVt18o-DvBuRRgyTygL2A/viewform

Source notes:

- Base docs describe Builder Grants as live, retroactive funding for shipped projects.
- Current grant range listed by Base docs: 1-5 ETH.
- The form asks for email, nominator name, project name, project URL, project Twitter, project Farcaster/channel, builder Twitter, builder Farcaster, whether the project is live on Base, a short justification, and a 1-minute demo link.

## Form Answers

### Email

`[IAN EMAIL]`

### Nominator Name

Ian Alloway

### Project Name

On-chain Risk Scanner

### Project URL

https://github.com/ianalloway/onchain-risk-scanner

### Project Twitter

`[PROJECT OR IAN X/TWITTER URL]`

### Project Farcaster/Channel

`[FARCASTER URL OR CHANNEL]`

### Builder Twitter

`[IAN X/TWITTER URL]`

### Builder Farcaster

`[IAN FARCASTER URL]`

### Is the project currently live on Base?

Yes - live on Base mainnet

Reason: the project is a shipped open-source scanner for Base mainnet contracts. It is not an on-chain protocol; it is developer/security tooling that reads Base mainnet data and publishes reproducible Base reports.

### Why does this project deserve a Base grant? 150 words max

On-chain Risk Scanner is shipped open-source security tooling for Base builders and users. It performs read-only contract triage through JSON-RPC and surfaces proxy metadata, privileged selectors, opcode-level risk signals, and upgrade/admin timelines in Markdown or JSON reports. The repo now includes multiple public Base scans and a roadmap for verified-source ingestion. A Base Builder Grant would fund the next milestone: a larger Base contract scan set and clearer tooling for developers to understand upgrade/admin risk before integrations. The project is non-custodial, uses no private keys, sends no transactions, and is designed as public-good security infrastructure.

Word count: 100

### Please link a 1 minute demo of the project

https://raw.githubusercontent.com/ianalloway/onchain-risk-scanner/main/demo/base-builder-grants-demo.mp4

Suggested demo outline:

1. Show the GitHub repo.
2. Run `onchain-risk 0x4200000000000000000000000000000000000006 --chain base`.
3. Open `examples/base-weth.md`.
4. Explain that the tool is read-only, open source, and designed for Base contract-risk education.

### Coinbase Multimedia License Checkbox

Only Ian should check this after uploading/using a demo video he owns.

### Marketing Communications

Ian decision.
