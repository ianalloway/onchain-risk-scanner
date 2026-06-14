# Public Scan Set

Generated with On-chain Risk Scanner as read-only public-chain triage. These reports are not audits and do not prove safety or exploitability. They show the kind of first-pass evidence a builder or security researcher can use before deeper manual review.

## Summary

| Report | Chain | Risk band | Reviewer takeaway |
| --- | --- | --- | --- |
| [Base WETH](base-weth.md) | Base | info | WETH-style bytecode with a low `ORIGIN` signal; useful as a baseline wrapped-native-token scan. |
| [Base USDC](base-usdc.md) | Base | low | Selector/opcode signals point to privileged upgrade-style surfaces worth source-level review. |
| [Base cbBTC](base-cbbtc.md) | Base | low | Similar upgrade-selector profile to other bridged/token contracts; good candidate for ABI/source enrichment. |
| [Ethereum WETH](ethereum-weth.md) | Ethereum | low | WETH mainnet baseline with `DELEGATECALL` present but no EIP-1967 storage metadata detected. |
| [Ethereum USDC](ethereum-usdc.md) | Ethereum | medium | Medium triage score driven by delegatecall/origin/privileged-selector signals; source review matters. |
| [Ethereum EntryPoint v0.6](ethereum-entrypoint-v06.md) | Ethereum | info | Large runtime bytecode but no heuristic findings in the current scanner profile. |
| [Optimism WETH](optimism-weth.md) | Optimism | info | Low-signal WETH-style baseline on OP Mainnet. |
| [Optimism USDC](optimism-usdc.md) | Optimism | low | Privileged-selector and delegatecall signals suggest manual review of upgrade/admin controls. |
| [Optimism L2 to L1 Message Passer](optimism-l2-to-l1-message-passer.md) | Optimism | medium | EIP-1967 proxy metadata detected; implementation/admin should be reviewed before integration assumptions. |
| [Arbitrum WETH](arbitrum-weth.md) | Arbitrum | medium | EIP-1967 proxy metadata and privileged selectors found; strong example of why proxy visibility matters. |
| [Arbitrum USDC](arbitrum-usdc.md) | Arbitrum | low | Privileged-selector and delegatecall signals without EIP-1967 storage metadata in this scan. |
| [Arbitrum ARB](arbitrum-arb.md) | Arbitrum | medium | EIP-1967 proxy metadata found, including implementation and admin addresses. |

## Upgrade/Admin Timelines

| Timeline | Range | Result |
| --- | --- | --- |
| [Base USDC timeline](base-usdc-timeline.md) | recent 1,000 blocks | No tracked upgrade/admin events found. |
| [Ethereum USDC timeline](ethereum-usdc-timeline.md) | recent 1,000 blocks | No tracked upgrade/admin events found. |
| [Optimism USDC timeline](optimism-usdc-timeline.md) | recent 1,000 blocks | No tracked upgrade/admin events found. |
| [Arbitrum USDC timeline](arbitrum-usdc-timeline.md) | recent 1,000 blocks | No tracked upgrade/admin events found. |

## Notes

- A clean or low score is not a safety guarantee.
- Privileged selectors may appear in proxy bytecode or embedded data and should be mapped to verified source in the next milestone.
- Timeline reports use a conservative 1,000-block default because many public RPCs reject large `eth_getLogs` ranges.
