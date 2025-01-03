import os
import re


REGEX = r"^mul\((\d{1,3}),(\d{1,3})\)"


def multiply(inpt: str) -> int:
    match = re.match(REGEX, inpt)
    if match:
        return int(match.group(1)) * int(match.group(2))
    return 0


def get_valid_expressions(inpt: str) -> list[str]:
    expressions = []
    for i in range(len(inpt)):
        match = re.search(REGEX, inpt[i:])
        if match:
            expressions.append(match.group())
    print(expressions)
    return expressions


def parse_multiply(inpt: str) -> list[int]:
    expressions = get_valid_expressions(inpt)
    return [multiply(e) for e in expressions]


def run(filepath: str):
    with open(filepath, encoding="utf8") as file:
        data = TEST_DATA if os.getenv("TEST") else file.read()
        results = parse_multiply(data)
        print(sum(results))


TEST_DATA = """
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""
