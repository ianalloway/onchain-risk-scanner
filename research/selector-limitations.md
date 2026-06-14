# Selector And Opcode Limitations

The scanner is intentionally lightweight. It is useful for first-pass triage, but it should not be treated as a full static analyzer.

## What It Does Well

- Detects runtime bytecode size.
- Counts selected EVM opcodes while skipping PUSH data for opcode hits.
- Checks EIP-1967 proxy storage slots.
- Flags common privileged selectors as review leads.
- Builds recent upgrade/admin timelines from public logs.

## Current Limits

- Selector matching is bytecode-level and should be mapped to ABI/source in the next milestone.
- Public RPCs can limit log ranges.
- Proxy patterns outside EIP-1967 may require additional detectors.
- A low score is not a safety guarantee.

## Next Technical Milestone

Verified-source and ABI ingestion should map selectors to source-level functions and reduce ambiguity. That is the most valuable next step for grant credibility and white-hat usefulness.
