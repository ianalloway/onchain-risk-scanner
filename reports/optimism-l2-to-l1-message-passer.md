# On-chain Risk Report: `0x4200000000000000000000000000000000000016`

- Chain: `optimism` (10)
- Explorer: https://optimistic.etherscan.io/address/0x4200000000000000000000000000000000000016
- Risk score: **46/100** (medium)
- Runtime bytecode: `2055` bytes
- Native balance: `85255.35091769` ETH

## Proxy

- Implementation: `0xc0d3c0d3c0d3c0d3c0d3c0d3c0d3c0d3c0d30016`
- Admin: `0x4200000000000000000000000000000000000018`
- Beacon: `not detected`

## Findings

### MEDIUM: DELEGATECALL present

Delegatecall can be legitimate for proxies and libraries, but it raises the impact of storage-layout and implementation-control bugs.

### LOW: Privileged selectors detected

Potential privileged entrypoints found in bytecode: changeAdmin(address), upgradeTo(address), upgradeToAndCall(address,bytes)

### MEDIUM: EIP-1967 proxy storage detected

Proxy metadata was found. Review admin controls, implementation history, initialization, and upgrade process before trusting assets.


## Opcode Hits

- `callcode`: 0
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
