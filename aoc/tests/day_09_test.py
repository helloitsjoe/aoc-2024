from aoc.day_09 import run, to_blocks, compact_blocks, get_checksum, TEST_DATA


def _to_ints(data: str) -> list[int]:
    return list(map(_replace_dot, data))


def _replace_dot(ea: str):
    return int(ea.replace(".", "-1"))


def test_to_blocks_basic():
    data = "12345"
    assert to_blocks(data) == _to_ints("0..111....22222")


def test_compact_blocks_basic():
    data = _to_ints("0..111....22222")
    assert compact_blocks(data) == _to_ints("022111222")


def test_checksum():
    data = _to_ints("022111222")
    assert get_checksum(data) == 60


def test_to_blocks_test_data():
    assert to_blocks(TEST_DATA) == _to_ints(
        "00...111...2...333.44.5555.6666.777.888899"
    )


def test_compact_blocks_test_data():
    data = _to_ints("00...111...2...333.44.5555.6666.777.888899")
    assert compact_blocks(data) == _to_ints("0099811188827773336446555566")


def test_checksum_test_data():
    data = _to_ints("0099811188827773336446555566")
    assert get_checksum(data) == 1928


def test_double_digit_id():
    data = "233313312141413140243"
    assert to_blocks(data) == [
        0,
        0,
        -1,
        -1,
        -1,
        1,
        1,
        1,
        -1,
        -1,
        -1,
        2,
        -1,
        -1,
        -1,
        3,
        3,
        3,
        -1,
        4,
        4,
        -1,
        5,
        5,
        5,
        5,
        -1,
        6,
        6,
        6,
        6,
        -1,
        7,
        7,
        7,
        -1,
        8,
        8,
        8,
        8,
        9,
        9,
        -1,
        -1,
        -1,
        -1,
        10,
        10,
        10,
    ]


def test_run():
    assert run(TEST_DATA) == 1928
