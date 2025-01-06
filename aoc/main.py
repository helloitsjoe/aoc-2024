import os
import string
from aoc.day_04 import run, TEST_DATA, DATA_FILE


def main():
    filepath = os.path.join(os.getcwd(), "aoc", DATA_FILE)
    with open(filepath, encoding="utf8") as file:
        data = TEST_DATA if os.getenv("TEST") else file.read()
        output = run(data)
        print(output)


if __name__ == "__main__":
    main()
