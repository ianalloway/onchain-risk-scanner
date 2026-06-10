# White-hat Playbook

This project should help you earn trust before it helps you earn money.

## Rules

- Stay inside published bug bounty scope.
- Use read-only calls unless a program explicitly authorizes testing transactions.
- Never move, freeze, or drain funds.
- Do not publish exploitable details before disclosure is complete.
- Keep notes, timestamps, inputs, outputs, and impact reasoning.

## Where To Hunt

| Platform | Use it for |
| --- | --- |
| Immunefi | Live crypto protocol bounties with high upside. |
| HackenProof | Web3 smart contract and app bug bounty programs. |
| Sherlock | Audit contests and competitive smart contract review. |
| Code4rena | Historical reports and remaining bounty programs, not the main future pipeline. |

## Beginner-Friendly Targets

Start with contracts where the scanner can guide manual review:

- upgradeable ERC-20s
- vaults with owner/admin controls
- pause/mint/withdraw flows
- oracle-fed accounting systems
- staking reward contracts

## Research Workflow

1. Pick an in-scope program.
2. Read the scope, reward table, excluded impacts, and disclosure rules.
3. Run the scanner on target contracts.
4. Manually inspect the highest-signal findings.
5. Try to prove realistic impact in a local fork or test environment.
6. Write the report with clear reproduction, impact, severity, and remediation.

## Report Template

```markdown
# Vulnerability Report

## Summary

One sentence explaining the bug and impact.

## Scope

- Program:
- Contract:
- Chain:
- Commit/address:

## Impact

Explain funds at risk, affected users, and realistic attacker path.

## Reproduction

Steps, commands, and proof-of-concept details that respect program rules.

## Root Cause

The exact code or design issue.

## Recommended Fix

Concrete mitigation.
```

## Skills To Build Next

- Solidity and EVM storage layout
- Foundry fork tests
- proxy upgrade patterns
- oracle manipulation and TWAPs
- access control models
- ERC-20 and ERC-4626 edge cases
- bridges and cross-chain message validation
