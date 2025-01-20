from aoc.day_08 import get_nodes, get_antinodes, parse_grid, TEST_DATA


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


def test_part_2_basic():
    data = """
......
......
..A...
...A..
......
......
"""
    grid = parse_grid(data)
    assert get_antinodes(get_nodes(grid), grid, True) == [
        (4, 4),
        (5, 5),
        (0, 0),
        (1, 1),
        (3, 3),
        (2, 2),
    ]


def test_part_2_complex():
    data = """
T.........
...T......
.T........
..........
..........
..........
..........
..........
..........
..........
"""

    # _with_antinodes = """
    # T....#....
    # ...T......
    # .T....#...
    # .........#
    # ..#.......
    # ..........
    # ...#......
    # ..........
    # ....#.....
    # ..........
    # """
    grid = parse_grid(data)
    antinodes = get_antinodes(get_nodes(grid), grid, True)
    assert antinodes == [
        (6, 2),
        (1, 2),
        (2, 4),
        (9, 3),
        (0, 0),
        (3, 1),
        (5, 0),
        (4, 8),
        (3, 6),
    ]
    assert len(antinodes) == 9


def test_test_data():
    grid = parse_grid(TEST_DATA)
    antinodes = get_antinodes(get_nodes(grid), grid)
    assert antinodes == [
        (0, 7),
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
        (6, 0),
        (10, 2),
        (9, 4),
    ]
    assert len(antinodes) == 14


def test_test_data_part_2():
    grid = parse_grid(TEST_DATA)
    antinodes = get_antinodes(get_nodes(grid), grid, True)
    assert antinodes == [
        (3, 1),
        (4, 9),
        (5, 7),
        (11, 5),
        (2, 2),
        (1, 0),
        (11, 11),
        (2, 8),
        (7, 7),
        (6, 5),
        (4, 2),
        (3, 3),
        (3, 6),
        (10, 2),
        (9, 4),
        (0, 7),
        (8, 8),
        (10, 11),
        (1, 5),
        (7, 3),
        (5, 2),
        (4, 4),
        (3, 11),
        (5, 5),
        (8, 1),
        (11, 0),
        (9, 9),
        (1, 1),
        (0, 0),
        (2, 3),
        (10, 10),
        (1, 10),
        (6, 0),
        (6, 6),
    ]
    assert len(antinodes) == 34
