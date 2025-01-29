import re
from typing import Callable

DATA_FILE = "day_13.txt"

TEST_DATA = """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""

type ButtonCoords = tuple[int, int]
type PrizeCoords = tuple[int, int]
type Machine = tuple[ButtonCoords, ButtonCoords, PrizeCoords]


def parse_machine(
    machine: str,
) -> Machine:
    a, b, prize = machine.splitlines()

    a_match = re.match(r"Button A: X\+(\d+), Y\+(\d+)", a)
    b_match = re.match(r"Button B: X\+(\d+), Y\+(\d+)", b)
    prize_match = re.match(r"Prize: X=(\d+), Y=(\d+)", prize)

    if a_match is None or b_match is None or prize_match is None:
        raise RuntimeError("bonk")

    (ax, ay) = a_match.group(1), a_match.group(2)
    (bx, by) = b_match.group(1), b_match.group(2)
    (prize_x, prize_y) = prize_match.group(1), prize_match.group(2)

    return (int(ax), int(ay)), (int(bx), int(by)), (int(prize_x), int(prize_y))


def get_num_tokens(part_2: bool) -> Callable:
    start = (10**10) if part_2 else 1
    end = (10**11) if part_2 else 100

    def get_num_tokens_inner(machine: Machine) -> tuple[int, int]:
        print("here")
        print("start", start)
        print("end", end)
        (ax, ay), (bx, by), (prize_x, prize_y) = machine

        tokens: list[tuple[int, int]] = []
        tokens_a: set[tuple[int, int]] = set()
        tokens_b: set[tuple[int, int]] = set()

        for b_x_presses in range(start, end):
            a_x_presses = (prize_x - (bx * b_x_presses)) / ax
            if a_x_presses < 0 or a_x_presses != int(a_x_presses):
                continue
            tokens_a.add((int(a_x_presses), b_x_presses))
            print(a_x_presses)

        for b_y_presses in range(start, end):
            a_y_presses = (prize_y - (by * b_y_presses)) / ay
            if a_y_presses < 0 or a_y_presses != int(a_y_presses):
                continue
            tokens_b.add((int(a_y_presses), b_y_presses))
            print(a_y_presses)

        tokens.extend(tokens_b.intersection(tokens_a))
        print(tokens)

        # for i in range(limit):
        #     for j in range(limit):
        #         if ax * i + bx * j == prize_x and ay * i + by * j == prize_y:
        #             tokens.append((i, j))

        minimum = min(tokens) if tokens else (0, 0)

        return minimum

    return get_num_tokens_inner


def run(data: str, part_2: bool = False):
    """
    You wonder: what is the smallest number of tokens you would have to spend to win as many prizes as possible?
    """
    machines = data.strip().split("\n\n")
    parsed = list(map(parse_machine, machines))
    num_tokens = list(map(get_num_tokens(part_2), parsed))
    return sum((a * 3 + b * 1 for a, b in num_tokens))
