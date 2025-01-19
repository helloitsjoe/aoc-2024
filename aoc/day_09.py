DATA_FILE = "day_09.txt"

TEST_DATA = "2333133121414131402"


def to_blocks(data: str) -> list[int]:
    blocks = []
    block_id = 0
    for i, block in enumerate(data):
        if i == 0 or i % 2 == 0:
            for _ in range(int(block)):
                blocks.append(block_id)
            block_id += 1
        else:
            for _ in range(int(block)):
                blocks.append(-1)

    # print(blocks)
    return blocks


def compact_blocks(data: list[int]) -> list[int]:
    data_list = data[:]
    num_ints = len(data) - data.count(-1)
    i = data_list.index(-1)

    while len(data_list) > num_ints:
        # Find the next empty space
        while data_list[i] != -1:
            i += 1
        last = data_list.pop()
        if last != -1:
            data_list[i] = last

    # print(data_list)
    return data_list


def get_checksum(blocks: list[int]) -> int:
    return sum((i * block_id for i, block_id in enumerate(blocks)))


def run(data: str):
    return get_checksum(compact_blocks(to_blocks(data.strip())))
