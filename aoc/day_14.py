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

type Robots = list[tuple[tuple[int, int], tuple[int, int]]]
type Floor = list[list[int]]


def parse_robots(data: str) -> Robots:
    lines = data.strip().splitlines()
    p_v: list[tuple[tuple[int, int], tuple[int, int]]] = []
    for line in lines:
        p, v = line.replace("p=", "").replace("v=", "").split(" ")
        x, y = p.split(",")
        v_x, v_y = v.split(",")
        p_v.append(((int(x), int(y)), (int(v_x), int(v_y))))

    return p_v


def tick(robots: Robots, w: int, h: int) -> Robots:
    rtn: Robots = []
    for (px, py), (vx, vy) in robots:
        next_x = px + vx
        next_y = py + vy
        if next_x >= w:
            next_x -= w
        if next_y >= h:
            next_y -= h
        rtn.append(((next_x, next_y), (vx, vy)))
    return rtn


def loop(initial_robots: Robots, w: int, h: int, times: int) -> Robots:
    robots = initial_robots
    for _ in range(times):
        robots = tick(robots, w, h)
    return robots


def count_robots(robots: Robots, w: int, h: int) -> int:
    count = 0
    for (px, py), _ in robots:
        if px != w // 2 and py != h // 2:
            count += 1
    return count


def run(data: str, part_2: bool = False):
    w = 101 if part_2 else 11
    h = 103 if part_2 else 7
    # floor = [list(range(width)) for row in range(height)]
    robots = parse_robots(data)

    return robots
