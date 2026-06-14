# On-chain Risk Report: `0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

- Chain: `ethereum` (1)
- Explorer: https://etherscan.io/address/0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48
- Risk score: **38/100** (medium)
- Runtime bytecode: `2186` bytes
- Native balance: `0.0` ETH

## Proxy

- No EIP-1967 proxy metadata detected.

## Findings

### MEDIUM: DELEGATECALL present

Delegatecall can be legitimate for proxies and libraries, but it raises the impact of storage-layout and implementation-control bugs.

### LOW: ORIGIN opcode present

tx.origin usage can be unsafe for authorization if used directly.

### LOW: Privileged selectors detected

Potential privileged entrypoints found in bytecode: changeAdmin(address), upgradeTo(address), upgradeToAndCall(address,bytes)


## Opcode Hits

- `callcode`: 0
- `delegatecall`: 1
- `origin`: 1
- `selfdestruct`: 0

## Selector Hits

- `0x3659cfe6`: `upgradeTo(address)`
- `0x4f1ef286`: `upgradeToAndCall(address,bytes)`
- `0x8f283970`: `changeAdmin(address)`

## Notes

- This scanner is read-only and does not prove exploitability.
- Treat findings as triage leads for manual review, not final audit results.
