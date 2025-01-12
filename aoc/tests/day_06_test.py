from aoc.day_06 import run, TEST_DATA


def test_basic():
    assert run(TEST_DATA) == (41, 0)


def test_basic_top():
    data = """
.^.
...
...
"""
    assert run(data) == (1, 0)


def test_basic_left():
    data = """
.#.
.^#
.#.
"""
    assert run(data) == (3, 0)


def test_basic_right():
    data = """
.#.
.^.
...
"""
    assert run(data) == (2, 0)


def test_loop():
    data = """
.#...
....#
.^...
#....
...#.
"""
    assert run(data) == (8, 1)
