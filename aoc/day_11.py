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


def process_stones(stones: list[str]) -> list[str]:
    new_stones = []

    for stone in stones:
        if stone == "0":
            new_stones.append("1")
        elif len(stone) % 2 == 0:
            half = int(len(stone) / 2)
            new_stones.extend([str(int(stone[:half])), str(int(stone[half:]))])
        else:
            new_stones.append(str(int(stone) * 2024))

    return new_stones


def blink(stones: list[str], times: int) -> list[str]:
    if times == 0:
        return stones

    new_stones = process_stones(stones)

    return blink(new_stones, times - 1)


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
    print(part_2)
    stones = data.strip().split(" ")
    return len(blink(stones, 25))
