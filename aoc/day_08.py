import os

type Nodes = dict[str, set[tuple[int, int]]]


def get_nodes(grid: list[list[str]]) -> Nodes:
    nodes: dict[str, set[tuple[int, int]]] = {}

    for y, row in enumerate(grid):
        for x, point in enumerate(row):
            if point != ".":
                if point not in nodes:
                    nodes[point] = set()
                nodes[point].add((x, y))
    return nodes


def is_on_grid(antinode: tuple[int, int], grid: list[list[str]]):
    (x, y) = antinode
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)


def get_antinodes(
    nodes: Nodes, grid: list[list[str]], part_2: bool = False
) -> list[tuple[int, int]]:
    """
    For each pair of nodes, find antinodes on either side
    """
    antinodes: set[tuple[int, int]] = set()

    for node_coords in nodes.values():
        for i, node1 in enumerate(node_coords):
            for j, node2 in enumerate(node_coords):
                if j <= i:
                    continue

                (x1, y1) = node1
                (x2, y2) = node2

                distance_x = abs(x1 - x2)
                distance_y = abs(y1 - y2)

                direction_x = 1 if x1 < x2 else -1
                direction_y = 1 if y1 < y2 else -1

                antinode1 = (
                    x2 + distance_x * direction_x,
                    y2 + distance_y * direction_y,
                )
                antinode2 = (
                    x1 - distance_x * direction_x,
                    y1 - distance_y * direction_y,
                )

                if is_on_grid(antinode1, grid):
                    antinodes.add(antinode1)
                if is_on_grid(antinode2, grid):
                    antinodes.add(antinode2)

    return list(antinodes)


def parse_grid(grid: str) -> list[list[str]]:
    return [list(line) for line in grid.strip().splitlines()]


def run(data: str):
    """
    find antinodes: points in-line with two nodes of the same letter that are
    double the distance between the two nodes.

    Return the total number of antinodes that are within the bounds of the map
    """
    grid = parse_grid(data)
    nodes = get_nodes(grid)
    antinodes = get_antinodes(nodes, grid, os.getenv("PART_2") == "true")

    return len(antinodes)


DATA_FILE = "day_08.txt"

TEST_DATA = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""
