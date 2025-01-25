from dataclasses import dataclass

DATA_FILE = "day_12.txt"

TEST_DATA = """
AAAA
BBCD
BBCC
EEEC
"""


# def get_area_and_perimeter(
#     land: list[list[str]],
#     letter: str,
#     areas: dict[str, int],
#     perimeters: dict[str, int],
# ):
#     for y, row in enumerate(land):
#         for x, sq in enumerate(row):


#     return area, perimeter


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
    x: int, y: int, land: list[list[Square]]
) -> tuple[str, int, int]:
    area = 0
    perimeter = 0
    curr = land[y][x]
    curr_x = x
    curr_y = y
    curr_letter = curr.val
    to_check = [(curr, x, y)]

    # TODO: Move to each next square... How to determine when there are no more
    # squares in the current plot?
    while to_check:
        for dir_x, dir_y in DIRS.values():
            next_x = curr_x + dir_x
            next_y = curr_y + dir_y

            if 0 <= next_y < len(land) and 0 <= next_x < len(land[y]):
                next_sq = land[next_y][next_x]
                if next_sq.visited or next_sq.val != curr.val:
                    continue

                print("appending", next_sq, next_x, next_y)
                to_check.append((next_sq, next_x, next_y))

                # Add to area
                area += 1

                # Add to perimeter
                #     Check each side
                #     Subtract 2 if same letter (should skip if visited?)
                # perimeter += 4

        # Mark as visited
        curr.visited = True
        # Move on
        (curr, curr_x, curr_y) = to_check.pop()

    print(area, perimeter)
    return curr_letter, area, perimeter


def get_plots(land: Land):
    plots: list[Plot] = []

    for y, row in enumerate(land):
        for x, sq in enumerate(row):
            print(row)
            if sq.visited:
                continue
            letter, area, perimeter = spread_from(x, y, land)
            plots.append((letter, area, perimeter))

    return plots


# def get_perimeters(land: list[list[Square]]):
#     perimeters: dict[str, int] = {}

#     for y, row in enumerate(land):
#         for x, letter in enumerate(row):
#             perimeters[letter] = perimeters.get(letter, 0) + 4
#             if 0 <= (x - 1) < len(land[y]) and land[y][x - 1] == letter:
#                 perimeters[letter] -= 2
#             if 0 <= (y - 1) < len(land) and land[y - 1][x] == letter:
#                 perimeters[letter] -= 2

#     return perimeters


def combine_area_and_perimeter(
    # areas: dict[str, int], perimeters: dict[str, int]
    plots: list[Plot],
):
    total = 0
    for letter, area, perimeter in plots:
        total += area * perimeter

    return total


def run(data: str, __part_2: bool = False):
    land = create_land(data)

    # areas = get_areas(land)
    # perimeters = get_perimeters(land)
    plots = get_plots(land)
    # print(areas)
    # print(perimeters)
    print(plots)

    return combine_area_and_perimeter(plots)
