# On-chain Risk Report: `0x0b2C639c533813f4Aa9D7837CAF62653d097Ff85`

- Chain: `optimism` (10)
- Explorer: https://optimistic.etherscan.io/address/0x0b2C639c533813f4Aa9D7837CAF62653d097Ff85
- Risk score: **30/100** (low)
- Runtime bytecode: `1852` bytes
- Native balance: `0.0` ETH

## Proxy

- No EIP-1967 proxy metadata detected.

## Findings

### MEDIUM: DELEGATECALL present

Delegatecall can be legitimate for proxies and libraries, but it raises the impact of storage-layout and implementation-control bugs.

### LOW: Privileged selectors detected

Potential privileged entrypoints found in bytecode: changeAdmin(address), upgradeTo(address), upgradeToAndCall(address,bytes)


## Opcode Hits

- `callcode`: 0
- `delegatecall`: 1
- `origin`: 0
- `selfdestruct`: 0

## Selector Hits

- `0x3659cfe6`: `upgradeTo(address)`
- `0x4f1ef286`: `upgradeToAndCall(address,bytes)`
- `0x8f283970`: `changeAdmin(address)`

## Notes

- This scanner is read-only and does not prove exploitability.
- Treat findings as triage leads for manual review, not final audit results.
