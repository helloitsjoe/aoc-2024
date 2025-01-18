DATA_FILE = "day_09.txt"

TEST_DATA = "2333133121414131402"


def to_blocks(data: str) -> str:
    blocks = []
    block_id = 0
    for i, block in enumerate(data):
        if i == 0 or i % 2 == 0:
            for _ in range(int(block)):
                blocks.append(str(block_id))
            block_id += 1
        else:
            for _ in range(int(block)):
                blocks.append(".")
    result = "".join(blocks)
    # print(result)
    return result


def compact_blocks(data: str) -> str:
    start_idx = 0
    end_idx = len(data) - 1
    compacted: list[str] = []
    num_ints = len(data) - data.count(".")

    while end_idx >= start_idx:
        print(end_idx, start_idx)

        while data[end_idx] == ".":
            end_idx -= 1

        while data[start_idx] != ".":
            if len(compacted) == num_ints:
                break
            compacted.append(data[start_idx])
            start_idx += 1

        if len(compacted) == num_ints:
            break

        compacted.append(data[end_idx])
        start_idx += 1
        end_idx -= 1

    result = "".join(compacted)
    # print(result)
    return result


def get_checksum(data: str) -> int:
    blocks = list(data.replace(".", ""))
    return sum((i * int(block_id) for i, block_id in enumerate(blocks)))


def run(data: str):
    return get_checksum(compact_blocks(to_blocks(data.strip())))
