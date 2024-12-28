import re


def part_1_get_sum(left: list[int], right: list[int]) -> int:
    return sum(abs(left_val - right[i]) for (i, left_val) in enumerate(left))


def part_2_get_similarity(left: list[int], right: list[int]):
    return sum(
        left_val * _get_counts(right).get(left_val, 0) for left_val in left
    )


def _get_counts(inp: list[int]) -> dict[int, int]:
    out: dict[int, int] = {}
    for num in inp:
        out[num] = out.get(num, 0) + 1
    return out


def _split_lists(lists: str) -> tuple[list[int], list[int]]:
    left: list[int] = []
    right: list[int] = []
    for line in list(lists.splitlines()):
        [left_num, right_num] = re.split(r"\s+", line)
        left.append(int(left_num))
        right.append(int(right_num))
    return (sorted(left), sorted(right))


def run(filepath: str):
    with open(filepath, encoding="utf8") as file:
        left, right = _split_lists(file.read())
        print(part_2_get_similarity(left, right))


TEST_INPUT = """3   4
4   3
2   5
1   3
3   9
3   3
"""
