# White-Hat Start List

Use this list to start earning credibility safely.

## Platform Accounts To Create

- Immunefi: https://immunefi.com/bug-bounty/
- HackenProof: https://hackenproof.com/programs
- Sherlock: https://audits.sherlock.xyz/contests

## First Hunt Criteria

Pick programs with:

- clear smart contract scope,
- public GitHub repo,
- deployed contract addresses,
- explicit safe harbor,
- clear reward table,
- simple protocol mechanics,
- no requirement to attack live funds.

Avoid first:

- bridges,
- complex cross-chain messaging,
- protocols with vague scope,
- reports requiring real mainnet transactions,
- programs with many duplicate historical findings.

## Selected Programs
See [selected-programs.md](selected-programs.md) for the list of selected white-hat bounty programs.

## Repeatable Workflow

1. Read the scope twice.
2. Save contract addresses and repo commit.
3. Run On-chain Risk Scanner.
4. Inspect privileged selectors, proxy metadata, and upgrade/admin risk.
5. Read source manually.
6. Reproduce only in a local fork/testnet environment.
7. Submit only if there is concrete impact and a clean proof.

## Report Hooks To Look For

- Unprotected initialization on upgradeable contracts.
- Owner/admin role can drain, mint, pause, or upgrade unexpectedly.
- Oracle price assumptions that can be manipulated.
- Accounting mismatch between shares and assets.
- Signature replay across chains/domains.
- Missing slippage, deadline, or recipient validation.
- Unsafe external calls before state updates.