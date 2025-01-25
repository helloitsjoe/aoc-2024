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


def convert_to_list(data: str):
    return [list(line) for line in data.strip().splitlines()]


def get_areas(land: list[list[str]]):
    areas: dict[str, int] = {}

    for row in land:
        for letter in row:
            areas[letter] = areas.get(letter, 0) + 1

    return areas


def get_perimeters(land: list[list[str]]):
    perimeters: dict[str, int] = {}

    for y, row in enumerate(land):
        for x, letter in enumerate(row):
            perimeters[letter] = perimeters.get(letter, 0) + 4
            if 0 <= (x - 1) < len(land[y]) and land[y][x - 1] == letter:
                perimeters[letter] -= 2
            if 0 <= (y - 1) < len(land) and land[y - 1][x] == letter:
                perimeters[letter] -= 2

    return perimeters


def combine_area_and_perimeter(
    areas: dict[str, int], perimeters: dict[str, int]
):
    total = 0
    for letter in areas:
        total += areas[letter] * perimeters[letter]

    return total


def run(data: str, __part_2: bool = False):
    land = convert_to_list(data)

    areas = get_areas(land)
    perimeters = get_perimeters(land)
    print(areas)
    print(perimeters)

    return combine_area_and_perimeter(areas, perimeters)
