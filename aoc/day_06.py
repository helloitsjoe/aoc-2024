import os

DIRECTIONS: dict[str, tuple[int, int]] = {
    "^": (0, -1),
    ">": (1, 0),
    "v": (0, 1),
    "<": (-1, 0),
}


def get_next_symbol(symbol: str):
    match symbol:
        case "^":
            return ">"
        case ">":
            return "v"
        case "v":
            return "<"
        case "<":
            return "^"


def parse_board(data: str) -> list[list[str]]:
    return [list(row) for row in list(data.strip().splitlines())]


def get_visited_length(board: list[list[str]]):
    """
    Counts the number of visited spaces before the guard leaves the board
    - Start at ^
    - Move in that direction until you reach a #
    - Count spaces (don't double count)
    - Turn 90deg right
    - Repeat until off board
    """
    symbol = "^"
    curr = [0, 0]
    visited: dict[str, str] = {}
    is_loop = False

    for y, row in enumerate(board):
        for x, val in enumerate(row):
            if val == symbol:
                curr = [x, y]
                break

    while 0 <= curr[1] < len(board) and 0 <= curr[0] < len(board[0]):
        x, y = curr[0], curr[1]
        if visited.get(f"{x}:{y}") == symbol:
            is_loop = True
            break
        visited[f"{x}:{y}"] = symbol
        next_x = x + DIRECTIONS[symbol][0]
        next_y = y + DIRECTIONS[symbol][1]

        if (
            next_y >= len(board)
            or next_x >= len(board[0])
            or next_y < 0
            or next_x < 0
        ):
            break
        while board[next_y][next_x] == "#":
            symbol = get_next_symbol(symbol)
            next_x = x + DIRECTIONS[symbol][0]
            next_y = y + DIRECTIONS[symbol][1]
        curr = [next_x, next_y]

    return (len(visited), is_loop)


def add_blockage(row: list[str], board: list[list[str]], x: int, y: int):
    new_x = x + 1
    new_y = y + 1
    new_row = row[:x] + ["#"] + row[new_x:]
    new_board = board[:y] + [new_row] + board[new_y:]
    return new_board


def get_num_loops(board: list[list[str]]):
    """
    Iterate through the board adding a new block at each empty space,
    and return the number of block positions that would result in a loop
    """
    loops = 0
    for y, row in enumerate(board):
        for x, val in enumerate(row):
            if val == ".":
                modified_board = add_blockage(row, board, x, y)
                _, is_loop = get_visited_length(modified_board)
                if is_loop:
                    print(x, y)
                    loops += 1
                    print("Loops:", loops)
    return loops


def run(data: str) -> int:
    board = parse_board(data)

    return (
        get_num_loops(board)
        if os.getenv("LOOP_CHECK")
        else get_visited_length(board)
    )


DATA_FILE = "day_06.txt"

TEST_DATA = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""
