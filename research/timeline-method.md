# Upgrade Timeline Method

The `timeline` subcommand searches public RPC logs for common EIP-1967/OpenZeppelin events:

- `Upgraded(address)`
- `AdminChanged(address,address)`
- `BeaconUpgraded(address)`

It uses `eth_getLogs`, so it remains read-only and does not require private keys.

## Why The Default Window Is Small

Many public RPC endpoints reject large log ranges. The default lookback is 1,000 blocks so the command works reliably with common public RPCs. Researchers can pass `--from-block` and `--to-block` when they have a better RPC endpoint.

## Current Scan Set

The current USDC timelines on Base, Ethereum, Optimism, and Arbitrum did not find tracked upgrade/admin events in the recent 1,000-block window. This should be read narrowly: it means no tracked events were observed in that window, not that the contract has never been upgraded.
