from dataclasses import dataclass

DATA_FILE = "day_12.txt"

TEST_DATA = """
AAAA
BBCD
BBCC
EEEC
"""


DIRS = {
    "N": (0, -1),
    "E": (1, 0),
    "S": (0, 1),
    "W": (-1, 0),
}


@dataclass
class Square:
    val: str
    visited: bool = False

    def __repr__(self):
        return f"{self.val} | {self.visited}"


type Land = list[list[Square]]
type Plot = tuple[str, int, int]


def create_land(data: str):
    return [list(map(Square, line)) for line in data.strip().splitlines()]


def spread_from(
    initial_x: int, initial_y: int, land: list[list[Square]]
) -> tuple[str, int, int]:
    area = 0
    perimeter = 0
    curr = land[initial_y][initial_x]

    to_check = [(curr, initial_x, initial_y)]

    while to_check:
        (curr, x, y) = to_check.pop()

        if not curr.visited:
            area += 1

            perimeter += 4
            if 0 <= (y - 1) < len(land) and land[y - 1][x].val == curr.val:
                perimeter -= 2
            if 0 <= (x - 1) < len(land[y]) and land[y][x - 1].val == curr.val:
                perimeter -= 2
        curr.visited = True

        for dir_x, dir_y in DIRS.values():
            next_x = x + dir_x
            next_y = y + dir_y

            if (
                next_y < 0
                or next_x < 0
                or next_y >= len(land)
                or next_x >= len(land[y])
            ):
                continue

            next_sq = land[next_y][next_x]
            if next_sq.visited or next_sq.val != curr.val:
                continue

            to_check.append((next_sq, next_x, next_y))

    return land[y][x].val, area, perimeter


def get_plots(land: Land):
    plots: list[Plot] = []

    for y, row in enumerate(land):
        for x, sq in enumerate(row):
            if sq.visited:
                continue
            letter, area, perimeter = spread_from(x, y, land)
            plots.append((letter, area, perimeter))

    return plots


def combine_area_and_perimeter(
    plots: list[Plot],
):
    total = 0
    for _, area, perimeter in plots:
        total += area * perimeter

    return total


def run(data: str, __part_2: bool = False):
    land = create_land(data)

    plots = get_plots(land)

    return combine_area_and_perimeter(plots)
