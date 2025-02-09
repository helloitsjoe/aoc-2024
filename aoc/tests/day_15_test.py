from aoc.day_15 import step, parse_input

DATA = """
#####
#@..#
#...#
#...#
#####

<<<
"""


def test_parse_input():
    room, moves = parse_input(DATA)
    assert room == [
        ["#", "#", "#", "#", "#"],
        ["#", "@", ".", ".", "#"],
        ["#", ".", ".", ".", "#"],
        ["#", ".", ".", ".", "#"],
        ["#", "#", "#", "#", "#"],
    ]
    assert moves == "<<<"


def test_step_blocked():
    room, _ = parse_input(DATA)
    start = (1, 1)
    curr, _ = step("<", start, room)
    assert curr == (1, 1)


def test_step_open():
    room, _ = parse_input(DATA)
    start = (1, 1)
    curr, _ = step(">", start, room)
    assert curr == (2, 1)


def test_step_box_move():
    data = """
#####
#@O.#
#####

>
"""
    room, _ = parse_input(data)
    start = (1, 1)
    curr, room = step(">", start, room)
    assert curr == (2, 1)
    assert "".join(room[1]) == "#.@O#"
