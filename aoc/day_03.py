import re

DATA_FILE = "day_03.txt"

REGEX = r"^mul\((\d{1,3}),(\d{1,3})\)"


def multiply(inpt: str) -> int:
    match = re.match(REGEX, inpt)
    if match:
        return int(match.group(1)) * int(match.group(2))
    return 0


def get_valid_expressions(inpt: str) -> list[str]:
    """
    Valid expressions are in the form `mul(x,y)` where x and y are ints between
    1 and 3 digits.

    Part 2: do() and don't() toggle subsequent expressions enabled/disabled
    """
    expressions = []
    enabled = True
    for i in range(len(inpt)):
        if re.search(r"^don't\(\)", inpt[i:]):
            enabled = False
        if re.search(r"^do\(\)", inpt[i:]):
            enabled = True
        if enabled:
            match = re.search(REGEX, inpt[i:])
            if match:
                expressions.append(match.group())

    print(expressions)
    return expressions


def parse_multiply(inpt: str) -> list[int]:
    expressions = get_valid_expressions(inpt)
    return [multiply(e) for e in expressions]


def run(data: str):
    results = parse_multiply(data)
    print(sum(results))


TEST_DATA = """
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""
