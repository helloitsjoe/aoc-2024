import math
import time

DATA_FILE = "day_11.txt"

# Initial arrangement:
# 125 17

# After 1 blink:
# 253000 1 7

# After 2 blinks:
# 253 0 2024 14168

# After 3 blinks:
# 512072 1 20 24 28676032

# After 4 blinks:
# 512 72 2024 2 0 2 4 2867 6032

# After 5 blinks:
# 1036288 7 2 20 24 4048 1 4048 8096 28 67 60 32

# After 6 blinks:
# 2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2

TEST_DATA = "125 17"


def process_stones(
    stones: list[int], memo: dict[int, tuple[int, int]] = {}
) -> list[int]:
    new_stones = []

    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        else:
            log_10 = math.floor(math.log10(stone)) + 1
            if log_10 % 2 == 0:
                if stone in memo:
                    new_stones.extend(memo[stone])
                else:
                    dividend = 10 ** (log_10 / 2)
                    left = math.floor(stone / dividend)
                    sub = int(left * dividend)
                    right = stone - sub
                    memo[stone] = (left, right)
                    new_stones.extend((left, right))
            else:
                new_stones.append(stone * 2024)

    return new_stones


def blink(stones: list[int], times: int) -> list[int]:
    # if times == 0:
    #     return stones

    # new_stones = process_stones(stones)

    # return blink(new_stones, times - 1)

    new_stones = stones[:]
    memo: dict[int, tuple[int, int]] = {}
    for _ in range(times):
        new_stones = process_stones(new_stones, memo)
        # print(new_stones)

    return new_stones


def run(data: str, part_2: bool = False):
    """
    Blinking stones

    - If the stone is engraved with the number 0, it is replaced by a stone
      engraved with the number 1.
    - If the stone is engraved with a number that has an even number of digits,
      it is replaced by two stones. The left half of the digits are engraved on
      the new left stone, and the right half of the digits are engraved on the
      new right stone. (The new numbers don't keep extra leading zeroes: 1000
      would become stones 10 and 0.)
    - If none of the other rules apply, the stone is replaced by a new stone;
      the old stone's number multiplied by 2024 is engraved on the new stone.

    Order is preserved

    Return number of stones after blinking 25 times
    """
    start = time.time()
    stones = list(map(int, data.strip().split(" ")))
    blinks = 75 if part_2 else 25
    length = len(blink(stones, blinks))
    print(time.time() - start)
    return length
