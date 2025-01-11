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


def run(data: str) -> int:
    """
    - Start at ^
    - Move in that direction until you reach a #
    - Count spaces (don't double count)
    - Turn 90deg right
    - Repeat until off board
    """
    symbol = "^"
    curr = [0, 0]
    visited = {}
    rows = list(data.strip().splitlines())
    board = [list(row) for row in rows]
    for y, _ in enumerate(board):
        for x in range(len(board)):
            if board[y][x] == symbol:
                curr = [x, y]
                visited[f"{x}:{y}"] = 1

    while 0 <= curr[1] < len(rows) and 0 <= curr[0] < len(rows[0]):
        x, y = curr[0], curr[1]
        visited[f"{x}:{y}"] = 1
        next_x = x + DIRECTIONS[symbol][0]
        next_y = y + DIRECTIONS[symbol][1]
        if len(board) <= next_y or len(board[y]) <= next_x:
            break
        while board[next_y][next_x] == "#":
            symbol = get_next_symbol(symbol)
            next_x = x + DIRECTIONS[symbol][0]
            next_y = y + DIRECTIONS[symbol][1]
        curr = [next_x, next_y]
    return len(visited)


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
