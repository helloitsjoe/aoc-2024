from aoc.day_13 import run, parse_machine, get_num_tokens, TEST_DATA


def test_parse_machine():
    data = """Button A: X+12, Y+45
Button B: X+30, Y+22
Prize: X=400, Y=600
"""
    assert parse_machine(data) == ((12, 45), (30, 22), (400, 600))


def test_get_num_tokens():
    data = ((94, 34), (22, 67), (8400, 5400))
    assert get_num_tokens(False)(data) == (80, 40)


def test_run():
    data = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400
"""
    assert run(data) == 280


# def test_run_part_2():
#     data = """Button A: X+26, Y+66
# Button B: X+67, Y+21
# Prize: X=10000000012748, Y=10000000012176"""
#     assert run(data, True) == 280


def test_run_test_data():
    assert run(TEST_DATA) == 480
