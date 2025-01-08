from aoc.day_05 import run, get_full_order, parse_orders, TEST_DATA

TEST_DATA_SMALL = """2|4
0|3
2|3
4|3
0|1
0|4
2|1
1|4
1|3
0|2
"""


def test_full_order_small():
    orders = parse_orders(TEST_DATA_SMALL)
    assert get_full_order(orders) == [0, 2, 1, 4, 3]


def test_full_order():
    orders = parse_orders(TEST_DATA.split("\n\n", maxsplit=1)[0])
    assert get_full_order(orders) == [97, 75, 47, 61, 53, 29, 13]


def test_run_correct():
    assert run(TEST_DATA, True) == 143


def test_run_incorrect():
    assert run(TEST_DATA, False) == 13
