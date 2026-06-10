from onchain_risk_scanner.heuristics import (
    analyze_bytecode,
    extract_address_from_storage,
    risk_band,
)


def test_extract_address_from_storage_returns_none_for_zero_slot() -> None:
    assert extract_address_from_storage("0x" + "0" * 64) is None


def test_extract_address_from_storage_reads_last_20_bytes() -> None:
    address = "1234567890abcdef1234567890abcdef12345678"
    slot = "0x" + "0" * 24 + address
    assert extract_address_from_storage(slot) == "0x" + address


def test_analyze_bytecode_detects_opcode_and_selector_hits() -> None:
    bytecode = "0x60006000f460003659cfe6ff"
    report = analyze_bytecode(bytecode)

    assert report.bytecode_bytes == 12
    assert report.opcode_hits["delegatecall"] == 1
    assert report.opcode_hits["selfdestruct"] == 1
    assert report.selector_hits["3659cfe6"] == "upgradeTo(address)"
    assert {finding.title for finding in report.findings} >= {
        "DELEGATECALL present",
        "SELFDESTRUCT present",
        "Privileged selectors detected",
    }


def test_analyze_bytecode_ignores_opcode_bytes_inside_push_data() -> None:
    bytecode = "0x63f4fff23200"
    report = analyze_bytecode(bytecode)

    assert report.opcode_hits["delegatecall"] == 0
    assert report.opcode_hits["selfdestruct"] == 0
    assert report.opcode_hits["callcode"] == 0
    assert report.opcode_hits["origin"] == 0


def test_empty_bytecode_is_reported_as_no_contract() -> None:
    report = analyze_bytecode("0x")
    assert report.bytecode_bytes == 0
    assert report.findings[0].title == "No contract bytecode"


def test_risk_bands() -> None:
    assert risk_band(0) == "info"
    assert risk_band(12) == "low"
    assert risk_band(35) == "medium"
    assert risk_band(70) == "high"
