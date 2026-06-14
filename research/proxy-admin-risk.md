# Proxy/Admin Risk Triage

Upgradeable contracts are common in production protocols, but their risk is not only in the user-facing functions. The scanner looks for EIP-1967 implementation, admin, and beacon storage slots because those values tell reviewers who can change the logic behind a stable address.

## What The Scan Set Shows

- [Arbitrum WETH](../reports/arbitrum-weth.md) exposes EIP-1967 proxy metadata, including implementation and admin addresses.
- [Arbitrum ARB](../reports/arbitrum-arb.md) also exposes EIP-1967 proxy metadata and privileged upgrade selectors.
- [Optimism L2 to L1 Message Passer](../reports/optimism-l2-to-l1-message-passer.md) shows why chain-system contracts deserve explicit upgrade/admin review.

## Safe Review Questions

- Who controls the admin?
- Is the admin a multisig, governance contract, timelock, or EOA?
- Has the implementation changed recently?
- Are users or integrators relying on immutability that the contract does not actually provide?

These are triage questions, not vulnerability claims.
