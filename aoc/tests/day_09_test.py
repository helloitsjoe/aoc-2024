from aoc.day_09 import to_blocks, compact_blocks, get_checksum, TEST_DATA


def test_to_blocks_basic():
    data = "12345"
    assert to_blocks(data) == "0..111....22222"


def test_compact_blocks_basic():
    data = "0..111....22222"
    assert compact_blocks(data) == "022111222"


def test_checksum():
    data = "022111222"
    assert get_checksum(data) == 60


def test_checksum_extra_dots():
    data = "022111222....."
    assert get_checksum(data) == 60


def test_to_blocks_test_data():
    assert to_blocks(TEST_DATA) == "00...111...2...333.44.5555.6666.777.888899"


def test_compact_blocks_test_data():
    data = "00...111...2...333.44.5555.6666.777.888899"
    assert compact_blocks(data) == "0099811188827773336446555566"


def test_checksum_test_data():
    data = "0099811188827773336446555566.............."
    assert get_checksum(data) == 1928
