from collections import namedtuple

DATA_FILE = "day_10.txt"

TEST_DATA = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""
N = (0, -1)
S = (0, 1)
E = (1, 0)
W = (-1, 0)

Square = namedtuple("Square", ["x", "y", "val", "children"])
Trail = namedtuple("Trail", ["start", "end"])


class Peaks:
    peak_set: set[Square]
    peak_list: list[Square]
    part_2: bool

    def __init__(self, part_2):
        self.part_2 = part_2
        self.peak_set = set()
        self.peak_list = []

    def add(self, sq: Square):
        if self.part_2:
            self.peak_list.append(sq)
        else:
            self.peak_set.add(sq)

    def __iter__(self):
        if self.part_2:
            yield from self.peak_list
        else:
            yield from self.peak_set
        # return self.peak_list if self.part_2 else self.peak_set

    def __len__(self):
        return len(self.peak_list) if self.part_2 else len(self.peak_set)


def dfs(
    sq: Square, data: list[list[int]], part_2: bool, target: int = 9
) -> Peaks:
    peaks = Peaks(part_2)

    for direction in [N, S, E, W]:
        x, y = direction
        next_y = sq.y + y
        next_x = sq.x + x
        if (
            next_y < 0
            or next_y >= len(data)
            or next_x < 0
            or next_x >= len(data[0])
        ):
            continue

        next_sq = data[next_y][next_x]
        if next_sq == sq.val + 1:
            if next_sq == target:
                peaks.add(Square(next_x, next_y, next_sq, None))
            else:
                sq.children.append(Square(next_x, next_y, next_sq, []))

    for child in sq.children:
        for p in dfs(child, data, part_2, target):
            peaks.add(p)

    return peaks


# find each 0
# DFS to find all 9s for that 0
# when list is done, sum
def run(data: str, part_2: bool = False):
    """
    Trailheads are 0s, peaks are 9s
    Each trailhead's score is the number of peaks reachable from it. Return
    the total score of the data: number of peaks reachable from trailheads
    on paths increasing by 1 each step (never diagonal)
    """
    data_list = [list(map(int, line)) for line in data.strip().splitlines()]

    total = 0
    for y, row in enumerate(data_list):
        for x, sq in enumerate(row):
            if sq == 0:
                peaks = dfs(Square(x, y, sq, []), data_list, part_2)
                total += len(peaks)

    return total
