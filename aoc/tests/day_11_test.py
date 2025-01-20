from aoc.day_11 import run, blink, process_stones, TEST_DATA


def test_process_stones_basic():
    assert process_stones(["0", "11", "1"]) == ["1", "1", "1", "2024"]


def test_process_stones_extra_zeros():
    assert process_stones(["0", "1000", "1"]) == ["1", "10", "0", "2024"]


def test_process_example():
    assert process_stones(["0", "1", "10", "99", "999"]) == [
        "1",
        "2024",
        "1",
        "0",
        "9",
        "9",
        "2021976",
    ]


def test_blink():
    assert blink(["0", "1000", "1"], 1) == ["1", "10", "0", "2024"]
    assert blink(["0", "1000", "1"], 2) == ["2024", "1", "0", "1", "20", "24"]


def test_run():
    assert run(TEST_DATA) == 55312
