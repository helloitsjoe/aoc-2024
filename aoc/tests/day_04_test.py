from aoc.day_04 import (
    join_vertical,
    join_horizontal,
    count,
    TEST_DATA,
)


TEST_DATA_SMALL = """
XXAMM
MMSMS
AAXAM
SAMMM
MXMXA
"""


def test_join_vertical_small():
    assert join_vertical(TEST_DATA_SMALL) == "XMASM XMAAX ASXMM MMAMX MSMMA"


def test_join_vertical():
    assert count(join_vertical(TEST_DATA)) == 3


def test_find_horizontal():
    assert count(join_horizontal(TEST_DATA)) == 5
