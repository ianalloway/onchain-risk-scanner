# On-chain Risk Report: `0x4200000000000000000000000000000000000006`

- Chain: `base` (8453)
- Explorer: https://basescan.org/address/0x4200000000000000000000000000000000000006
- Risk score: **8/100** (info)
- Runtime bytecode: `2041` bytes
- Native balance: `288518.73964756` ETH

## Proxy

- No EIP-1967 proxy metadata detected.

## Findings

### LOW: ORIGIN opcode present

tx.origin usage can be unsafe for authorization if used directly.


## Opcode Hits

- `callcode`: 0
- `delegatecall`: 0
- `origin`: 1
- `selfdestruct`: 0

## Selector Hits

- `0x23b872dd`: `transferFrom(address,address,uint256)`
- `0x2e1a7d4d`: `withdraw(uint256)`
- `0xa9059cbb`: `transfer(address,uint256)`

## Notes

- This scanner is read-only and does not prove exploitability.
- Treat findings as triage leads for manual review, not final audit results.
