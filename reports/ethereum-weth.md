# On-chain Risk Report: `0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2`

- Chain: `ethereum` (1)
- Explorer: https://etherscan.io/address/0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2
- Risk score: **18/100** (low)
- Runtime bytecode: `3124` bytes
- Native balance: `2599378.09757265` ETH

## Proxy

- No EIP-1967 proxy metadata detected.

## Findings

### MEDIUM: DELEGATECALL present

Delegatecall can be legitimate for proxies and libraries, but it raises the impact of storage-layout and implementation-control bugs.


## Opcode Hits

- `callcode`: 0
- `delegatecall`: 1
- `origin`: 0
- `selfdestruct`: 0

## Selector Hits

- `0x23b872dd`: `transferFrom(address,address,uint256)`
- `0x2e1a7d4d`: `withdraw(uint256)`
- `0xa9059cbb`: `transfer(address,uint256)`

## Notes

- This scanner is read-only and does not prove exploitability.
- Treat findings as triage leads for manual review, not final audit results.
