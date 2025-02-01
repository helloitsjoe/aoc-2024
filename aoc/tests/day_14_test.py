from aoc.day_14 import (
    run,
    parse_robots,
    count_robots,
    get_safety_factor,
    tick,
    loop,
    TEST_DATA,
)


def test_tick():
    data = "p=0,0 v=1,1"
    robots = parse_robots(data)
    tick_1 = tick(robots, w=3, h=3)
    tick_2 = tick(tick_1, w=3, h=3)
    assert tick_1 == [((1, 1), (1, 1))]
    assert tick_2 == [((2, 2), (1, 1))]


def test_tick_wrap():
    data = "p=2,1 v=1,1"
    robots = parse_robots(data)
    assert tick(robots, 3, 3) == [((0, 2), (1, 1))]


def test_tick_wrap_negative():
    data = "p=0,0 v=-1,-1"
    robots = parse_robots(data)
    assert tick(robots, 3, 3) == [((2, 2), (-1, -1))]


def test_tick_wrap_large():
    data = "p=2,1 v=5,5"
    robots = parse_robots(data)
    assert tick(robots, w=3, h=3) == [((1, 0), (5, 5))]


def test_tick_wrap_negative_large():
    data = "p=2,1 v=-5,-5"
    robots = parse_robots(data)
    assert tick(robots, w=3, h=3) == [((0, 2), (-5, -5))]


def test_loop():
    data = "p=0,0 v=1,1"
    robots = parse_robots(data)
    looped = loop(robots, 3, 3, 2)
    assert looped == [((2, 2), (1, 1))]


def test_count_robots():
    data = """
p=0,0 v=1,1
p=2,2 v=1,1
p=0,2 v=1,1
p=2,0 v=1,1
p=1,0 v=1,1
p=0,1 v=1,1
"""
    robots = parse_robots(data)
    assert count_robots(robots, w=3, h=3) == (1, 1, 1, 1)


def test_get_safety_factor():
    assert get_safety_factor((1, 1, 1, 1)) == 1
    assert get_safety_factor((1, 2, 3, 4)) == 24


def test_run():
    assert run(TEST_DATA) == 12
