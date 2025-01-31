DATA_FILE = "day_14.txt"

TEST_DATA = """
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""


def parse_robots(data: str) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    lines = data.strip().splitlines()
    p_v: list[tuple[tuple[int, int], tuple[int, int]]] = []
    for line in lines:
        p, v = line.replace("p=", "").replace("v=", "").split(" ")
        x, y = p.split(",")
        v_x, v_y = v.split(",")
        p_v.append(((int(x), int(y)), (int(v_x), int(v_y))))

    return p_v


def run(data: str, part_2: bool = False):
    width = 101 if part_2 else 11
    height = 103 if part_2 else 7
    floor = [list(range(width)) for row in range(height)]
    robots = parse_robots(data)
    return robots
