from aoc.day_08 import run, get_nodes, get_antinodes, parse_grid, TEST_DATA


def test_basic_grid():
    data = """
..0
0..
.A.
"""
    assert get_nodes(parse_grid(data)) == {
        "0": [(2, 0), (0, 1)],
        "A": [(1, 2)],
    }


def test_basic_antinodes():
    data = """
A...
.A..
....
"""
    assert get_antinodes(get_nodes(parse_grid(data))) == [(2, 2)]
