from aoc.day_09 import (
    run,
    to_blocks,
    compact_blocks,
    compact_file_blocks,
    move_file_blocks,
    create_block_map,
    create_slot_map,
    get_checksum,
    FileBlock,
    OpenBlock,
    TEST_DATA,
)


# Test helpers
def _to_ints(data: str) -> list[int]:
    return list(map(_replace_dot, data))


def _replace_dot(ea: str):
    return int(ea.replace(".", "-1"))


def _to_str(data: list[int]) -> str:
    return "".join(list(map(str, data))).replace("-1", ".")


def test_to_str():
    assert _to_str([1, -1, -1, 3]) == "1..3"


def test_to_blocks_basic():
    assert _to_str(to_blocks("12345")) == "0..111....22222"


def test_to_blocks_test_data():
    assert (
        _to_str(to_blocks(TEST_DATA))
        == "00...111...2...333.44.5555.6666.777.888899"
    )


def test_compact_blocks_basic():
    data = _to_ints("0..111....22222")
    assert _to_str(compact_blocks(data)) == "022111222"


def test_compact_blocks_test_data():
    data = _to_ints("00...111...2...333.44.5555.6666.777.888899")
    assert _to_str(compact_blocks(data)) == "0099811188827773336446555566"


def test_slot_map_basic():
    orig_data = "1112321"
    data = to_blocks(orig_data)
    assert _to_str(data) == "0.1..222..3"
    assert create_slot_map(data) == [(1, 1), (3, 2), (8, 2)]


def test_block_map_basic():
    orig_data = "1112321"
    data = to_blocks(orig_data)
    assert _to_str(data) == "0.1..222..3"
    assert create_block_map(data) == [
        FileBlock(idx=0, len=1, id=0),
        FileBlock(idx=2, len=1, id=1),
        FileBlock(idx=5, len=3, id=2),
        FileBlock(idx=10, len=1, id=3),
    ]


def test_move_file_blocks():
    orig_data = "1112321"
    data = to_blocks(orig_data)
    assert data == [0, -1, 1, -1, -1, 2, 2, 2, -1, -1, 3]
    slot_map = create_slot_map(data)
    block_map = create_block_map(data)
    assert (
        _to_str(move_file_blocks(data, slot_map, block_map)) == "031..222..."
    )


def test_move_file_blocks_partial():
    orig_data = "1312321"
    data = to_blocks(orig_data)
    assert data == [0, -1, -1, -1, 1, -1, -1, 2, 2, 2, -1, -1, 3]
    slot_map = create_slot_map(data)
    block_map = create_block_map(data)
    assert (
        _to_str(move_file_blocks(data, slot_map, block_map)) == "031....222..."
    )


def test_move_file_blocks_2():
    orig_data = "111232133"
    data = to_blocks(orig_data)
    assert data == [0, -1, 1, -1, -1, 2, 2, 2, -1, -1, 3, -1, -1, -1, 4, 4, 4]
    slot_map = create_slot_map(data)
    block_map = create_block_map(data)
    assert _to_str(move_file_blocks(data, slot_map, block_map)) == (
        "031..222...444..."
    )


def test_compact_file_blocks_basic():
    orig_data = "1112321"
    data = to_blocks(orig_data)
    assert data == [0, -1, 1, -1, -1, 2, 2, 2, -1, -1, 3]
    compacted = compact_file_blocks(data)
    assert _to_str(compacted) == "031..222..."


def test_slot_block_map_test_data():
    data = to_blocks(TEST_DATA)
    assert _to_str(data) == "00...111...2...333.44.5555.6666.777.888899"
    slot_map = create_slot_map(data)
    assert slot_map == [
        OpenBlock(idx=2, cap=3),
        OpenBlock(idx=8, cap=3),
        OpenBlock(idx=12, cap=3),
        OpenBlock(idx=18, cap=1),
        OpenBlock(idx=21, cap=1),
        OpenBlock(idx=26, cap=1),
        OpenBlock(idx=31, cap=1),
        OpenBlock(idx=35, cap=1),
    ]
    block_map = create_block_map(data)
    assert block_map == [
        FileBlock(idx=0, len=2, id=0),
        FileBlock(idx=5, len=3, id=1),
        FileBlock(idx=11, len=1, id=2),
        FileBlock(idx=15, len=3, id=3),
        FileBlock(idx=19, len=2, id=4),
        FileBlock(idx=22, len=4, id=5),
        FileBlock(idx=27, len=4, id=6),
        FileBlock(idx=32, len=3, id=7),
        FileBlock(idx=36, len=4, id=8),
        FileBlock(idx=40, len=2, id=9),
    ]


def test_compact_file_blocks_test():
    data = to_blocks(TEST_DATA)
    assert _to_str(data) == "00...111...2...333.44.5555.6666.777.888899"
    compacted = compact_file_blocks(data)
    assert _to_str(compacted) == "00992111777.44.333....5555.6666.....8888.."


def test_checksum():
    data = _to_ints("022111222")
    assert get_checksum(data) == 60


def test_checksum_test_data():
    data = _to_ints("0099811188827773336446555566")
    assert get_checksum(data) == 1928


def test_checksum_test_data_ignore_empty():
    data = [1, 0, -1, 3]
    assert get_checksum(data) == 9


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
    assert run(TEST_DATA, False) == 1928


def test_run_part_2():
    part_2 = True
    assert run(TEST_DATA, part_2) == 2858
