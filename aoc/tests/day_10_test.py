from aoc.day_10 import run, TEST_DATA


def test_basic():
    data = """
0123
3514
4415
9876
"""
    assert run(data) == 1


def test_multiple_paths_same_peak():
    data = """
0123
1514
2345
9876
"""
    assert run(data) == 1


def test_multiple_peaks():
    data = """
9990999
9991999
9992999
6543456
7111117
8111118
9111119
"""
    assert run(data) == 2


def test_run():
    assert run(TEST_DATA) == 36
