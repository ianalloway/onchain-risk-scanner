# Contributing

Thanks for helping make on-chain security review more accessible.

## Local Setup

```bash
git clone https://github.com/ianalloway/onchain-risk-scanner.git
cd onchain-risk-scanner
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -e ".[dev]"
python3 -m pytest
```

## Good First Contributions

- Add public scan reports with short, non-exploitative takeaways.
- Improve selector coverage.
- Add chain profiles.
- Improve timeline/event decoding.
- Improve docs around safe white-hat workflows.

## Report Guidelines

Reports should be read-only and educational. Avoid exploit instructions, private information, or claims that a contract is safe. Prefer language like “triage lead,” “manual review point,” and “observed signal.”

## Pull Request Checklist

- Tests pass with `python3 -m pytest`.
- New behavior has focused tests.
- README or docs are updated when user-facing behavior changes.
- No secrets, private keys, API keys, or private grant materials are committed.
