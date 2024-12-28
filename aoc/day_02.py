def two_window(start_idx: int, items: list[int]) -> tuple[int, int | None]:
    if len(items) == start_idx + 1:
        return items[start_idx], None
    return items[start_idx], items[start_idx + 1]


def find_safe(level: list[int]) -> bool:
    """
    level is determined safe if:
        1. The levels are either all increasing or all decreasing.
        2. Any two adjacent levels differ by at least one and at most three.

    """
    direction = "inc" if level[0] < level[1] else "dec"
    for i in range(len(level)):
        prev, curr = two_window(i, level)
        if curr is None:
            return True
        if (direction == "inc" and curr <= prev) or curr - prev > 3:
            return False
        if (direction == "dec" and prev <= curr) or prev - curr > 3:
            return False
    return True


def run(filepath: str):
    with open(filepath, encoding="utf8") as file:
        levels = [level.split(" ") for level in file.read().splitlines()]
        maybe_safe = [find_safe(list(map(int, level))) for level in levels]
        print(sum(safe is True for safe in maybe_safe))


TEST_DATA = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""
