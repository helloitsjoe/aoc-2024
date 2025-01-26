from aoc.day_12 import run, get_plots, create_land

TEST_DATA_SMALL = """
AAAA
BBCD
BBCC
EEEC
"""

TEST_DATA_MED = """
OOOOO
OXOXO
OOOOO
OXOXO
OOOOO
"""

TEST_DATA_LARGE = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""

test_data_small_list = create_land(TEST_DATA_SMALL)
test_data_med_list = create_land(TEST_DATA_MED)
test_data_large_list = create_land(TEST_DATA_LARGE)


def test_get_plots_small():
    assert get_plots(test_data_small_list) == [
        ("A", 4, 10),
        ("B", 4, 8),
        ("C", 4, 10),
        ("D", 1, 4),
        ("E", 3, 8),
    ]


def test_get_plots_med():
    assert get_plots(test_data_med_list) == [
        ("O", 21, 36),
        ("X", 1, 4),
        ("X", 1, 4),
        ("X", 1, 4),
        ("X", 1, 4),
    ]


def test_small():
    assert run(TEST_DATA_SMALL) == 140


def test_medium():
    assert run(TEST_DATA_MED) == 772


def test_large():
    assert run(TEST_DATA_LARGE) == 1930
