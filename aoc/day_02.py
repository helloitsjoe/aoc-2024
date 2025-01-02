import os


def two_window(start_idx: int, items: list[int]) -> tuple[int, int | None]:
    if len(items) == start_idx + 1:
        return items[start_idx], None
    return items[start_idx], items[start_idx + 1]


def find_safe(level: list[int], dampen: bool = False) -> bool:
    """
    level is determined safe if:
        1. The levels are either all increasing or all decreasing.
        2. Any two adjacent levels differ by at least one and at most three.

    if dampened is true, find_safe can tolerate one unsafe value
    """
    print(level)
    _dir = "inc" if level[0] < level[1] else "dec"

    for i in range(len(level)):
        prev, curr = two_window(i, level)
        if curr is None:
            return True

        valid_increasing = (_dir == "inc" and curr <= prev) or curr - prev > 3
        valid_decreasing = (_dir == "dec" and prev <= curr) or prev - curr > 3

        if (valid_increasing) or (valid_decreasing):
            if not dampen:
                return False
            for x in range(len(level)):
                y = x + 1
                # iterate to skip each potential unsafe value to tolerate
                result = find_safe(level[:x] + level[y:])
                if result is True:
                    return True
            return False
    return True


def run(filepath: str):
    with open(filepath, encoding="utf8") as file:
        # levels = [level.split(" ") for level in TEST_DATA.splitlines()]
        data = TEST_DATA if os.getenv("TEST") else file.read()
        levels = [level.split(" ") for level in data.splitlines()]
        maybe_safe = [
            (level, find_safe(list(map(int, level)), True)) for level in levels
        ]
        print(maybe_safe)
        print(sum(safe is True for _, safe in maybe_safe))


TEST_DATA = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
35 37 38 41 43 41
42 45 46 45 47 51
"""
