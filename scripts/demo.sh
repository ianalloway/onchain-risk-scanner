#!/usr/bin/env bash
set -euo pipefail

ADDRESS="${1:-0x4200000000000000000000000000000000000006}"
CHAIN="${2:-base}"

echo "On-chain Risk Scanner demo"
echo "Repo: https://github.com/ianalloway/onchain-risk-scanner"
echo
echo "Scanning ${ADDRESS} on ${CHAIN}..."
echo

onchain-risk "${ADDRESS}" --chain "${CHAIN}"
