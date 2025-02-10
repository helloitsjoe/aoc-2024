DATA_FILE = "day_15.txt"

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

TEST_DATA = """
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
"""

Dir = {
    "<": (-1, 0),
    ">": (1, 0),
    "^": (0, -1),
    "v": (0, 1),
}


def find_empty_space(
    start: tuple[int, int], direction: tuple[int, int], room: list[list[str]]
) -> tuple[int, int] | None:
    x, y = start
    dir_x, dir_y = direction

    # TODO:
    # ['#', 'O', '#', '@', '.', '.', '.', '#'] should be
    # ['#', '.', '#', 'O', '@', '.', '.', '#']

    if dir_x == 1:
        for i, sq in enumerate(room[y][x:]):
            if sq == ".":
                return x + i, y

    if dir_x == -1:
        # include @ at x + 1
        for i, sq in enumerate(reversed(room[y][: x + 1])):
            if sq == ".":
                return x - i, y

    if dir_y == 1:
        for j, row in enumerate(room[y:]):
            if row[x] == ".":
                return x, y + j

    if dir_y == -1:
        for j, row in enumerate(reversed(room[: y + 1])):
            if row[x] == ".":
                return x, y - j

    return None


def step(
    move: str, curr: tuple[int, int], room: list[list[str]]
) -> tuple[tuple[int, int], list[list[str]]]:
    x, y = curr
    dir_x, dir_y = Dir[move][0], Dir[move][1]
    next_x = x + dir_x
    next_y = y + dir_y

    empty_space = find_empty_space(curr, (dir_x, dir_y), room)

    if empty_space is None:
        return curr, room

    empty_x, empty_y = empty_space
    room[y][x] = "."
    if room[next_y][next_x] == "O":
        room[empty_y][empty_x] = "O"
        # room[next_y + dir_y][next_x + dir_x] = "O"

    room[next_y][next_x] = "@"
    return (next_x, next_y), room


def walk(room: list[list[str]], moves: str):
    curr = (0, 0)
    for y, row in enumerate(room):
        for x, sq in enumerate(row):
            if sq == "@":
                curr = (x, y)

    for move in moves:
        curr, room = step(move, curr, room)

    return room


def parse_input(data: str) -> tuple[list[list[str]], str]:
    room_input, moves = data.strip().split("\n\n")
    room = [list(row) for row in room_input.strip().splitlines()]
    return room, moves


def run(data: str, part_2: bool):
    room, moves = parse_input(test_data_small)
    room = walk(room, moves)
    return room
