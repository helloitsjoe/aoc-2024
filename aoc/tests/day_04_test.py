from aoc.day_04 import (
    run,
    join_vertical,
    join_horizontal,
    join_diagonal,
    count,
    count_cross,
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


def test_join_diagonal_small():
    assert join_diagonal(TEST_DATA_SMALL) == "XMXMA XSAM MAMX"
    assert join_diagonal(TEST_DATA_SMALL, True) == "MMXAM MSAS SAMX"


def test_count_vertical():
    assert count(join_vertical(TEST_DATA)) == 3


def test_count_horizontal():
    assert count(join_horizontal(TEST_DATA)) == 5


def test_count_diagonal():
    assert (
        count(join_diagonal(TEST_DATA)) + count(join_diagonal(TEST_DATA, True))
        == 10
    )


def test_count_cross():
    assert count_cross(TEST_DATA) == 9


def test_run():
    assert run(TEST_DATA) == 18


def test_run_part_2():
    assert run(TEST_DATA, True) == 9
