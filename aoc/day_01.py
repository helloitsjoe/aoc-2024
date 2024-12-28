import re
import os


def part_1_get_sum(left: list[int], right: list[int]) -> int:
    total = 0
    for i, left_item in enumerate(left):
        diff = abs(left_item - right[i])
        total += diff
    return total


def part_2_get_similarity(left: list[int], right: list[int]):
    total = 0
    right_counts = _get_counts(right)
    for left_val in left:
        print(left_val)
        total += left_val * right_counts.get(left_val, 0)
    return total


def _get_counts(inp: list[int]) -> dict[int, int]:
    out: dict[int, int] = {}
    for num in inp:
        curr_count = out.get(num, 0)
        out[num] = curr_count + 1
    print(out)
    return out


def _split_lists(lists: str) -> tuple[list[int], list[int]]:
    left: list[int] = []
    right: list[int] = []
    for line in list(lists.splitlines()):
        [left_num, right_num] = re.split(r"\s+", line)
        left.append(int(left_num))
        right.append(int(right_num))
    return (sorted(left), sorted(right))


def run():
    filepath = os.path.join(os.getcwd(), "aoc", "day_01.txt")
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
