import re

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


def get_num_tokens(machine: Machine) -> tuple[int, int]:
    (ax, ay), (bx, by), (prize_x, prize_y) = machine

    tokens = []

    for i in range(100):
        for j in range(100):
            if ax * i + bx * j == prize_x and ay * i + by * j == prize_y:
                tokens.append((i, j))

    minimum = min(tokens) if tokens else (0, 0)

    return minimum


def run(data: str, part_2: bool = False):
    """
    You wonder: what is the smallest number of tokens you would have to spend to win as many prizes as possible?
    """
    machines = data.strip().split("\n\n")
    parsed = list(map(parse_machine, machines))
    num_tokens = list(map(get_num_tokens, parsed))
    return sum((a * 3 + b * 1 for a, b in num_tokens))
