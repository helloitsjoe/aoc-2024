import os


def get_all_outputs(
    inputs: list[int],
    with_concat: bool = False,
) -> list[int]:
    """
    Return every combination of adding and multiplying the inputs
    """
    outputs = []

    if len(inputs) == 1:
        outputs.append(inputs[0])
        return outputs

    a, b, *rest = inputs
    first_sum = a + b
    first_product = a * b
    first_concat = int(f"{a}{b}")

    outputs_1 = get_all_outputs([first_sum, *rest], with_concat)
    outputs_2 = get_all_outputs([first_product, *rest], with_concat)
    if with_concat:
        outputs_3 = get_all_outputs([first_concat, *rest], with_concat)
        return [*outputs_1, *outputs_2, *outputs_3]

    return [*outputs_1, *outputs_2]


def parse_line(line: str):
    val, inputs = line.split(": ")
    return list(map(int, [val, *inputs.split(" ")]))


def parse_input(data: str):
    return [parse_line(line) for line in data.strip().splitlines()]


def run(data: str):
    """
    Data includes values on the left and numbers which can potentially produce
    the value when combined with + or *. Expressions are evaluated L-to-R,
    NOT by precedence rules.

    Return the sum of the values that can be produced correctly
    """
    parsed = parse_input(data)
    results: list[int] = []
    for line in parsed:
        val, *inputs = line
        outputs = get_all_outputs(inputs, os.getenv("PART_2") == "true")
        print(outputs)
        if val in outputs:
            results.append(val)
    return sum(results)


DATA_FILE = "day_07.txt"


# Answer: 3749 (190 + 3267 + 292)
TEST_DATA = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""
