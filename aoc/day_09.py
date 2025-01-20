import os
from collections import namedtuple

DATA_FILE = "day_09.txt"

TEST_DATA = "2333133121414131402"

FileBlock = namedtuple("FileBlock", ["idx", "len", "id"])


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


# TODO: make this clearer
def create_slot_map(data_list: list[int]) -> list[tuple[int, int]]:
    slot_map = []
    start_idx = -1
    cap = 0

    for i, block in enumerate(data_list):
        if block == -1:
            start_idx = i if start_idx == -1 else start_idx
            cap += 1
        else:
            if start_idx != -1:
                slot_map.append((start_idx, cap))
            start_idx = -1
            cap = 0

    if start_idx != -1:
        slot_map.append((start_idx, cap))

    return slot_map


def create_block_map(data_list: list[int]) -> list[FileBlock]:
    block_map = []
    start_idx = -1
    seen_block = -1
    cap = 0

    for i, block in enumerate(data_list):
        if block != -1:
            start_idx = i if start_idx == -1 else start_idx
            seen_block = block
            print(seen_block)
            cap += 1
        else:
            if start_idx != -1:
                block_map.append(FileBlock(start_idx, cap, seen_block))
            start_idx = -1
            cap = 0
            seen_block = -1

    # Add any blocks at the end
    if start_idx != -1 and seen_block != -1:
        block_map.append(FileBlock(start_idx, cap, seen_block))

    return block_map


def move_file_blocks(
    data_list: list[int],
    slot_map: list[tuple[int, int]],
    block_map: list[FileBlock],
) -> list[int]:
    # Iterate once over data_list, trying to fit each into first empty slot

    # Iterate backwards through data_list, looking only at full blocks
    for block in block_map[::-1]:
        print("block", block)
        for i, ea in enumerate(slot_map):
            idx, cap = ea
            print(block.len, cap)
            if block.len == cap:
                # fill slot and update idx, cap, and remove from data_list
                print("slot_map before", slot_map)
                slot_map = slot_map[0:i] + slot_map[i + 1 :]
                print("slot_map after", slot_map)

                print("data_list before", data_list)
                data_list = (
                    data_list[:idx]
                    + [block.id for _ in range(block.len)]
                    + data_list[i + block.len + 1 : block.idx]
                    + [-1 for _ in range(block.len)]
                    + data_list[block.idx + block.len :]
                )
                print("data_list after", data_list)
            elif block.len < cap:
                # remove len from cap
                # print("slot_map before", slot_map)
                # slot_map[i] = (i, cap - block.len)
                # print("slot_map after", slot_map)

                # # add block to beginning, remove from end
                # print("data_list before", data_list)
                # data_list = (
                #     data_list[:idx]
                #     + [block.id for _ in range(block.len)]
                #     + data_list[i + block.len + 1 : block.idx]
                #     + [-1 for _ in range(block.len)]
                #     + data_list[block.idx + block.len :]
                # )
                # print("data_list after", data_list)
                break

    return data_list


def compact_file_blocks(data: list[int], data_map: str) -> list[int]:
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


def run(data: str):
    data_map = data.strip()
    part_2 = os.getenv("PART_2") == "true"
    if part_2:
        return get_checksum(compact_file_blocks(to_blocks(data_map), data_map))
    return get_checksum(compact_blocks(to_blocks(data.strip())))
