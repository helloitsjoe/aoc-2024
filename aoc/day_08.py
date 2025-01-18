type Nodes = dict[str, list[tuple[int, int]]]


def get_nodes(grid: list[list[str]]) -> Nodes:
    nodes: dict[str, list[tuple[int, int]]] = {}

    for y, row in enumerate(grid):
        for x, point in enumerate(row):
            if point != ".":
                if point not in nodes:
                    nodes[point] = []
                nodes[point].append((x, y))

    return nodes


def get_antinodes(nodes: Nodes) -> list[tuple[int, int]]:
    """
    For each pair of nodes, find antinodes on either side
    """
    antinodes: list[tuple[int, int]] = []
    print(nodes.keys())
    for node1 in nodes.keys():
        for node2 in nodes.values():
            print(node1, node2)
            if node1 == node2:
                continue

            (x1, y1) = node1
            (x2, y2) = node2

            distance_x = abs(x1 - x2)
            distance_y = abs(y1 - y2)

            print(distance_x)
            print(distance_y)
            # antinode1 =
            # antinode2 =

    return antinodes


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
    antinodes = get_antinodes(nodes)

    return sum(antinodes)


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
