DATA_FILE = "day_04.txt"


def join_horizontal(data: str):
    return " ".join(data.splitlines())


def join_vertical(data: str):
    joined_vertical = ""
    rows = data.strip().splitlines()
    for y in range(len(rows)):
        for x in range(len(rows[0])):
            joined_vertical += rows[x][y]
        joined_vertical += " "
    return joined_vertical.strip()


# def join_diagonal(data: str):
#     joined_diagonal = ""
#     rows = data.strip().splitlines()
#     for y in range(len(rows)):
#         for x in range(len(rows[0])):
#             joined_diagonal += rows[x][y]
#         joined_diagonal += " "
#     return joined_diagonal.strip()


def count(data: str):
    total = 0
    for i in range(len(data)):
        end = i + 4
        if data[i:end] == "XMAS" or data[i:end] == "SAMX":
            total += 1
    return total


def run(data: str):
    """
    Prints the number of instances of XMAS in the input
    """
    total = sum(
        (
            count(join_horizontal(data)),
            count(join_vertical(data)),
            # count(join_diagonal(data)),
        )
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
