from aoc.day_06 import run, parse_board, get_num_loops, add_blockage, TEST_DATA


def test_basic():
    assert run(TEST_DATA) == (41, False)


def test_basic_top():
    data = """
.^.
...
...
"""
    assert run(data) == (1, False)


def test_basic_left():
    data = """
.#.
.^#
.#.
"""
    assert run(data) == (3, False)


def test_basic_right():
    data = """
.#.
.^.
...
"""
    assert run(data) == (2, False)


def test_loop():
    data = """
.#...
....#
.^...
#....
...#.
"""
    assert run(data) == (8, True)


def test_add_blockage():
    data = """
..
..
"""
    board = parse_board(data)
    row = board[0]
    new_board = add_blockage(row, board, 1, 0)
    assert new_board == [[".", "#"], [".", "."]]
    # Should make a copy
    assert new_board is not board


def test_num_loops():
    data = """
.#...
.....
.^...
#....
...#.
"""
    assert get_num_loops(parse_board(data)) == 1


def test_num_loops_2():
    data = """
....
#..#
.^#.
....
"""
    assert get_num_loops(parse_board(data)) == 1


def test_num_loops_3():
    data = """
....
..#.
#^..
.#..
"""
    assert get_num_loops(parse_board(data)) == 1


def test_num_loops_test_data():
    assert get_num_loops(parse_board(TEST_DATA)) == 6
