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


def join_diagonal(data: str, right_to_left: bool = False):
    joined_diagonal = ""
    rows = data.strip().splitlines()
    if right_to_left:
        rows = [row[::-1] for row in rows]

    for i in range(len(rows[0])):
        y = 0
        x = i
        remaining_letters = len(rows[y][x:])
        while y < len(rows):
            if x < len(rows) and remaining_letters >= 4:
                joined_diagonal += rows[y][x]
                y += 1
                x += 1
            else:
                break
        joined_diagonal += " "
    joined_diagonal = joined_diagonal.strip() + " "

    for i in range(len(rows)):
        y = i + 1
        x = 0
        remaining_letters = len(rows[y:][x:])
        while y < len(rows):
            if x < len(rows) and remaining_letters >= 4:
                joined_diagonal += rows[y][x]
                y += 1
                x += 1
            else:
                break
        joined_diagonal += " "

    return joined_diagonal.strip()


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
            count(join_diagonal(data)),
            count(join_diagonal(data, True)),
        )
    )
    print(total)
    return total


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
