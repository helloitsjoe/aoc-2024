from aoc.day_11 import run, blink, process_stones, TEST_DATA


def test_process_stones_basic():
    stones = {0: 1, 11: 1, 1: 1}
    assert process_stones(stones) == {1: 3, 2024: 1}


def test_process_stones_extra_zeros():
    stones = {0: 1, 1: 1, 1000: 1}
    assert process_stones(stones) == {1: 1, 10: 1, 0: 1, 2024: 1}


def test_process_example():
    stones = {
        0: 1,
        1: 1,
        10: 1,
        99: 1,
        999: 1,
    }
    assert process_stones(stones) == {
        1: 2,
        2024: 1,
        0: 1,
        9: 2,
        2021976: 1,
    }


def test_blink():
    stones = {0: 1, 1: 1, 1000: 1}
    assert blink(stones, 1) == {1: 1, 10: 1, 0: 1, 2024: 1}
    assert blink(stones, 2) == {1: 2, 0: 1, 20: 1, 24: 1, 2024: 1}


def test_run():
    assert run(TEST_DATA) == 55312
