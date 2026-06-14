# Security Policy

On-chain Risk Scanner is read-only tooling for public blockchain data. It does not send transactions, manage keys, custody funds, or attempt exploitation.

## Responsible Use

- Only test systems where you have authorization.
- Stay inside published bug bounty or audit-contest scope.
- Do not move, freeze, drain, or otherwise interfere with funds.
- Do not publish exploitable details before a disclosure process is complete.
- Treat scanner findings as triage leads, not proof of exploitability.

## Reporting Issues

For issues in this repository, open a GitHub issue when the report is not sensitive.

For sensitive security concerns, email:

`ian@allowayllc.com`

Please include:

- affected version or commit,
- command used,
- expected behavior,
- actual behavior,
- impact,
- safe reproduction steps.

## Scope

In scope:

- scanner bugs,
- incorrect or misleading report output,
- unsafe documentation,
- dependency or packaging issues.

Out of scope:

- vulnerabilities in third-party contracts scanned by this tool,
- live exploitation of protocols,
- reports requiring private keys or mainnet transactions.
