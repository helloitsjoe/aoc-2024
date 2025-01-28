import os
from aoc.day_13 import run, TEST_DATA, DATA_FILE


def main():
    filepath = os.path.join(os.getcwd(), "aoc", DATA_FILE)
    with open(filepath, encoding="utf8") as file:
        data = TEST_DATA if os.getenv("TEST") else file.read()
        part_2 = os.getenv("PART_2") == "true"
        output = run(data, part_2)
        print(output)


if __name__ == "__main__":
    main()
