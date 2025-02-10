from aoc.day_15 import (
    walk,
    step,
    parse_input,
    get_gps_sum,
    stringify,
    TEST_DATA,
)

DATA = """
#####
#@..#
#...#
#...#
#####

<<<
"""


def create_wide_input(inside: str):
    return f"""
{"#" * len(inside)}
{inside}
{"#" * len(inside)}

>
"""


def test_get_gps_sum():
    data = """
####
#O.#
#.O#
####

<
"""
    room, _ = parse_input(data)
    assert get_gps_sum(room) == 303


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
    assert curr == start


def test_step_open():
    room, _ = parse_input(DATA)
    start = (1, 1)
    curr, _ = step(">", start, room)
    assert curr == (2, 1)


def test_step_box_single_move():
    room, _ = parse_input(create_wide_input("#@O..#"))
    start = (1, 1)
    curr, room = step(">", start, room)
    assert curr == (2, 1)
    assert "".join(room[1]) == "#.@O.#"


def test_step_box_single_blocked():
    room, _ = parse_input(create_wide_input("#@O###"))
    start = (1, 1)
    curr, room = step(">", start, room)
    assert curr == start
    assert "".join(room[1]) == "#@O###"


def test_step_box_move():
    room, _ = parse_input(create_wide_input("#@OO.#"))
    start = (1, 1)
    curr, room = step(">", start, room)
    assert curr == (2, 1)
    assert "".join(room[1]) == "#.@OO#"


def test_step_box_blocked():
    room, _ = parse_input(create_wide_input("#@OO##"))
    start = (1, 1)
    curr, room = step(">", start, room)
    assert curr == start
    assert "".join(room[1]) == "#@OO##"


def test_step_box_blocked_hollow():
    room, _ = parse_input(create_wide_input("#@O#.#"))
    start = (1, 1)
    curr, room = step(">", start, room)
    assert "".join(room[1]) == "#@O#.#"
    assert curr == start


def test_step_box_move_left():
    room, _ = parse_input(create_wide_input("#.OO@#"))
    start = (4, 1)
    curr, room = step("<", start, room)
    assert curr == (3, 1)
    assert "".join(room[1]) == "#OO@.#"


def test_step_box_blocked_left():
    room, _ = parse_input(create_wide_input("#@OO##"))
    start = (1, 1)
    curr, room = step(">", start, room)
    assert curr == start
    assert "".join(room[1]) == "#@OO##"


def test_step_box_move_down():
    data = """
###
#@#
#O#
#O#
#.#
###

>
"""
    room, _ = parse_input(data)
    start = (1, 1)
    curr, room = step("v", start, room)
    assert curr == (1, 2)
    assert "".join(room[0]) == "###"
    assert "".join(room[1]) == "#.#"
    assert "".join(room[2]) == "#@#"
    assert "".join(room[3]) == "#O#"
    assert "".join(room[4]) == "#O#"
    assert "".join(room[5]) == "###"


def test_step_box_move_up():
    data = """
###
#.#
#O#
#O#
#@#
###

>
"""
    room, _ = parse_input(data)
    start = (1, 4)
    curr, room = step("^", start, room)
    assert curr == (1, 3)
    assert "".join(room[0]) == "###"
    assert "".join(room[1]) == "#O#"
    assert "".join(room[2]) == "#O#"
    assert "".join(room[3]) == "#@#"
    assert "".join(room[4]) == "#.#"
    assert "".join(room[5]) == "###"


def test_walk():
    test_data_small = """
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
    """
    room, moves = parse_input(test_data_small)
    room = walk(room, moves)
    assert (
        stringify(room)
        == """
########
#....OO#
##.....#
#.....O#
#.#O@..#
#...O..#
#...O..#
########
"""
    )


def test_walk_test_data():
    room, moves = parse_input(TEST_DATA)
    room = walk(room, moves)
    assert (
        stringify(room)
        == """
##########
#.O.O.OOO#
#........#
#OO......#
#OO@.....#
#O#.....O#
#O.....OO#
#O.....OO#
#OO....OO#
##########
"""
    )
