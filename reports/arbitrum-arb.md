# On-chain Risk Report: `0x912CE59144191C1204E64559FE8253a0e49E6548`

- Chain: `arbitrum` (42161)
- Explorer: https://arbiscan.io/address/0x912CE59144191C1204E64559FE8253a0e49E6548
- Risk score: **46/100** (medium)
- Runtime bytecode: `2593` bytes
- Native balance: `0.0` ETH

## Proxy

- Implementation: `0xd47d14a315394ddf063174f2286ab4eb7c507fa0`
- Admin: `0xdb216562328215e010f819b5abe947bad4ca961e`
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
- `delegatecall`: 3
- `origin`: 0
- `selfdestruct`: 0

## Selector Hits

- `0x3659cfe6`: `upgradeTo(address)`
- `0x4f1ef286`: `upgradeToAndCall(address,bytes)`
- `0x8f283970`: `changeAdmin(address)`

## Notes

- This scanner is read-only and does not prove exploitability.
- Treat findings as triage leads for manual review, not final audit results.
