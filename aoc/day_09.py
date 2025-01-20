from collections import namedtuple

DATA_FILE = "day_09.txt"

TEST_DATA = "2333133121414131402"

FileBlock = namedtuple("FileBlock", ["idx", "len", "id"])
OpenBlock = namedtuple("OpenBlock", ["idx", "cap"])


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


def create_slot_map(data_list: list[int]) -> list[OpenBlock]:
    slot_map = []
    start_idx = -1
    cap = 0

    for i, block in enumerate(data_list):
        if block == -1:
            start_idx = i if start_idx == -1 else start_idx
            cap += 1
        else:
            if start_idx != -1:
                slot_map.append(OpenBlock(start_idx, cap))
            start_idx = -1
            cap = 0

    if start_idx != -1:
        slot_map.append(OpenBlock(start_idx, cap))

    return slot_map


def create_block_map(data_list: list[int]) -> list[FileBlock]:
    block_map = []
    start_idx = -1
    seen_block = -1
    length = 0

    for i, block in enumerate(data_list):
        if block != -1:
            if seen_block not in (-1, block):
                block_map.append(FileBlock(start_idx, length, seen_block))
                start_idx = -1
                length = 0
            start_idx = i if start_idx == -1 else start_idx
            seen_block = block
            length += 1
        else:
            if start_idx != -1:
                block_map.append(FileBlock(start_idx, length, seen_block))
            start_idx = -1
            length = 0
            seen_block = -1

    # Add any blocks at the end
    if start_idx != -1 and seen_block != -1:
        block_map.append(FileBlock(start_idx, length, seen_block))

    return block_map


def move_file_blocks(
    data_list: list[int],
    slot_map: list[OpenBlock],
    block_map: list[FileBlock],
) -> list[int]:
    # Iterate once over data_list, trying to fit each into first empty slot
    for block in block_map[::-1]:
        for i, ea in enumerate(slot_map):
            idx, cap = ea
            if block.idx < idx:
                break
            if block.len <= cap:
                print("id", block.id)
                # remove len from cap
                slot_map[i] = OpenBlock(idx + block.len, cap - block.len)

                # add block to beginning, remove from end
                data_list = (
                    data_list[:idx]
                    + [block.id for _ in range(block.len)]
                    + data_list[idx + block.len : block.idx]
                    + [-1 for _ in range(block.len)]
                    + data_list[block.idx + block.len :]
                )
                break

    return data_list


def compact_file_blocks(data: list[int]) -> list[int]:
    data_list = data[:]

    # Map of empty slots (index of data_list, capacity)
    slot_map = create_slot_map(data_list)
    block_map = create_block_map(data_list)
    return move_file_blocks(
        data_list,
        slot_map,
        block_map,
    )


def get_checksum(blocks: list[int]) -> int:
    return sum(
        (i * block_id for i, block_id in enumerate(blocks) if block_id != -1)
    )


def run(data: str, part_2: bool = False):
    blocks = to_blocks(data.strip())
    compacted = (
        compact_file_blocks(blocks) if part_2 else compact_blocks(blocks)
    )
    return get_checksum(compacted)
