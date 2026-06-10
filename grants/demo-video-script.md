# 1-Minute Demo Video Script

Use this for the Base Builder Grants demo field.

## Setup

```bash
cd /Users/ianalloway/Documents/Codex/onchain-risk-scanner
source .venv/bin/activate
./scripts/demo.sh
```

## Script

Hi, I’m Ian. This is On-chain Risk Scanner, an open-source read-only CLI for Base and Ethereum contract triage.

The tool fetches public chain data through JSON-RPC, so it does not need private keys and does not send transactions.

Here I’m scanning the canonical WETH-style contract on Base. The report shows the chain, explorer link, bytecode size, proxy metadata, opcode hits, selector hits, and a risk score.

The goal is to help builders and security learners quickly identify where manual review should start: proxy/admin controls, privileged functions, and unusual bytecode signals.

The next milestone is a public set of Base scan reports, verified-source ingestion, and upgrade/admin timelines for safer integrations.

Repo: https://github.com/ianalloway/onchain-risk-scanner
