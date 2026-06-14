# On-chain Risk Report: `0x82aF49447D8a07e3bd95BD0d56f35241523fBab1`

- Chain: `arbitrum` (42161)
- Explorer: https://arbiscan.io/address/0x82aF49447D8a07e3bd95BD0d56f35241523fBab1
- Risk score: **64/100** (medium)
- Runtime bytecode: `2092` bytes
- Native balance: `163007.21892719` ETH

## Proxy

- Implementation: `0x8b194beae1d3e0788a1a35173978001acdfba668`
- Admin: `0xd570ace65c43af47101fc6250fd6fc63d1c22a86`
- Beacon: `not detected`

## Findings

### MEDIUM: DELEGATECALL present

Delegatecall can be legitimate for proxies and libraries, but it raises the impact of storage-layout and implementation-control bugs.

### HIGH: CALLCODE present

CALLCODE is legacy behavior and often signals unusual execution risk.

### LOW: Privileged selectors detected

Potential privileged entrypoints found in bytecode: changeAdmin(address), upgradeTo(address), upgradeToAndCall(address,bytes)

### MEDIUM: EIP-1967 proxy storage detected

Proxy metadata was found. Review admin controls, implementation history, initialization, and upgrade process before trusting assets.


## Opcode Hits

- `callcode`: 1
- `delegatecall`: 2
- `origin`: 0
- `selfdestruct`: 0

## Selector Hits

- `0x3659cfe6`: `upgradeTo(address)`
- `0x4f1ef286`: `upgradeToAndCall(address,bytes)`
- `0x8f283970`: `changeAdmin(address)`

## Notes

- This scanner is read-only and does not prove exploitability.
- Treat findings as triage leads for manual review, not final audit results.
