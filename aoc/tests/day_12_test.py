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

test_data_small_list = create_land(TEST_DATA_SMALL)
test_data_med_list = create_land(TEST_DATA_MED)


def test_get_plots_small():
    assert sorted(get_plots(test_data_small_list)) == [
        ("A", 4, 10),
        ("B", 4, 8),
        ("C", 4, 10),
        ("D", 1, 4),
        ("E", 3, 8),
    ]


# def test_get_areas_small():
#     areas = {"A": 4, "B": 4, "C": 4, "D": 1, "E": 3}
#     assert get_areas(test_data_small_list) == areas


# def test_get_areas_med():
#     areas = {"O": 21, "X": 4}
#     assert get_areas(test_data_med_list) == areas


# def test_get_perimeters_small():
#     perimeters = {"A": 10, "B": 8, "C": 10, "D": 4, "E": 8}
#     assert get_perimeters(test_data_small_list) == perimeters


# def test_get_perimeters_med():
#     perimeters = {"O": 36, "X": 16}
#     assert get_perimeters(test_data_med_list) == perimeters


# def test_small():
#     assert run(TEST_DATA_SMALL) == 140


# def test_medium():
#     assert run(TEST_DATA_MED) == 772


# def test_large():
#     data = TEST_DATA
