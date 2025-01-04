DATA_FILE = "day_04.txt"


def find_horizontal(data: str):
    total = 0
    joined = " ".join(data.splitlines())
    for i in range(len(joined)):
        end = i + 4
        if joined[i:end] == "XMAS":
            total += 1
        if joined[i:end] == "SAMX":
            total += 1
    return total


def find_vertical(data: str):
    total = 0
    joined_vertical = ""
    rows = data.splitlines()
    # for y in range(len(rows)):
    #     for x in range(len(rows[0])):
    #         # joined_vertical +=

    for i in range(len(joined_vertical)):
        end = i + 4
        if joined_vertical[i:end] == "XMAS":
            total += 1
        if joined_vertical[i:end] == "SAMX":
            total += 1
    return total


def find_diagonal(data: str):
    return 1


def run(data: str):
    """
    Prints the number of instances of XMAS in the input
    """
    total = sum(
        (find_horizontal(data), find_vertical(data), find_diagonal(data))
    )
    print(total)


TEST_DATA = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""
