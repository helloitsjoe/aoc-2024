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


def stringify(room: list[list[str]], wrap: bool = True) -> str:
    result = "\n".join(["".join(row) for row in room])
    return "\n" + result + "\n" if wrap else result


def get_box_gps(coords: tuple[int, int]) -> int:
    x, y = coords
    return 100 * y + x


def get_gps_sum(room: list[list[str]]) -> int:
    return sum(
        get_box_gps((x, y))
        for y, row in enumerate(room)
        for x, sq in enumerate(row)
        if sq == "O"
    )


def find_empty_space(
    start: tuple[int, int], direction: tuple[int, int], room: list[list[str]]
) -> tuple[int, int] | None:
    x, y = start
    dir_x, dir_y = direction

    while 0 <= x < len(room[0]) and 0 <= y < len(room):
        x += dir_x
        y += dir_y
        if room[y][x] == "#":
            return None
        if room[y][x] == ".":
            return x, y

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
    moves = "".join(moves.splitlines())
    return room, moves


def run(data: str, part_2: bool):
    room, moves = parse_input(data)
    room = walk(room, moves)
    print(stringify(room))
    gps_sum = get_gps_sum(room)
    return gps_sum
