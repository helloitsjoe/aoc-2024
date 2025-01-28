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


def parse_machine(
    machine: str,
) -> tuple[ButtonCoords, ButtonCoords, PrizeCoords]:
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


def run(data: str, part_2: bool):
    """
    You wonder: what is the smallest number of tokens you would have to spend to win as many prizes as possible?
    """
    machines = data.strip().split("\n\n")
    parsed = list(map(parse_machine, machines))
    return parsed
