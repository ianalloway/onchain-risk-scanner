from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Chain:
    name: str
    chain_id: int
    explorer: str
    public_rpc: str | None = None


CHAINS: dict[str, Chain] = {
    "ethereum": Chain(
        name="ethereum",
        chain_id=1,
        explorer="https://etherscan.io/address/",
        public_rpc="https://eth.llamarpc.com",
    ),
    "base": Chain(
        name="base",
        chain_id=8453,
        explorer="https://basescan.org/address/",
        public_rpc="https://mainnet.base.org",
    ),
    "optimism": Chain(
        name="optimism",
        chain_id=10,
        explorer="https://optimistic.etherscan.io/address/",
        public_rpc="https://mainnet.optimism.io",
    ),
    "arbitrum": Chain(
        name="arbitrum",
        chain_id=42161,
        explorer="https://arbiscan.io/address/",
        public_rpc="https://arb1.arbitrum.io/rpc",
    ),
}


def get_chain(name: str) -> Chain:
    key = name.lower().strip()
    if key not in CHAINS:
        supported = ", ".join(sorted(CHAINS))
        raise ValueError(f"Unsupported chain '{name}'. Supported: {supported}")
    return CHAINS[key]
