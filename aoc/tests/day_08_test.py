from aoc.day_08 import run, get_nodes, get_antinodes, parse_grid, TEST_DATA


def test_basic_grid():
    data = """
..0
0..
.A.
"""
    assert get_nodes(parse_grid(data)) == {
        "0": set([(2, 0), (0, 1)]),
        "A": set([(1, 2)]),
    }


def test_basic_antinodes():
    data = """
A...
.A..
....
"""
    grid = parse_grid(data)
    assert get_antinodes(get_nodes(grid), grid) == [(2, 2)]


def test_long_antinodes():
    data = """
A.....
..A...
......
"""
    grid = parse_grid(data)
    assert get_antinodes(get_nodes(grid), grid) == [(4, 2)]


def test_ne_sw_antinodes():
    data = """
......
..A...
A.....
"""
    grid = parse_grid(data)
    assert get_antinodes(get_nodes(grid), grid) == [(4, 0)]


def test_horizontal_antinodes():
    data = """
.......
..A.A..
.......
"""
    grid = parse_grid(data)
    assert get_antinodes(get_nodes(grid), grid) == [(0, 1), (6, 1)]


def test_vertical_antinodes():
    data = """
....
....
.A..
....
.A..
....
....
"""
    grid = parse_grid(data)
    assert get_antinodes(get_nodes(grid), grid) == [(1, 0), (1, 6)]


def test_middle_antinodes():
    data = """
......
..A...
...A..
......
"""
    grid = parse_grid(data)
    assert get_antinodes(get_nodes(grid), grid) == [(1, 0), (4, 3)]


def test_middle_ne_sw_antinodes():
    data = """
......
...A..
..A...
......
"""
    grid = parse_grid(data)
    assert get_antinodes(get_nodes(grid), grid) == [(4, 0), (1, 3)]


def test_non_empty_antinodes():
    data = """
......
..A...
...A..
....0.
"""
    grid = parse_grid(data)
    assert get_antinodes(get_nodes(grid), grid) == [(1, 0), (4, 3)]


def test_test_data():
    grid = parse_grid(TEST_DATA)
    antinodes = get_antinodes(get_nodes(grid), grid)
    assert antinodes == [
        (0, 7),
        (6, 0),
        (10, 11),
        (7, 7),
        (6, 5),
        (1, 5),
        (3, 1),
        (11, 0),
        (4, 2),
        (2, 3),
        (10, 10),
        (3, 6),
        (10, 2),
        (9, 4),
    ]
    assert len(antinodes) == 14
