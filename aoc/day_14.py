from functools import reduce
import os

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
        if next_x >= w or next_x < 0:
            next_x = next_x % w
        if next_y >= h or next_y < 0:
            next_y = next_y % h
        rtn.append(((next_x, next_y), (vx, vy)))
    return rtn


def draw(robots: Robots, w: int, h: int, i: int) -> None:
    should_print = False
    found = False
    floor = [[" " for _ in range(w)] for row in range(h)]
    for (px, py), _ in robots:
        floor[py][px] = "X"

    # Look for a pattern with diagonals
    for y, row in enumerate(floor):
        if found:
            break
        for x, sq in enumerate(row):
            if (
                sq == "X"
                and y - 4 > 0
                and x - 4 > 0
                and y + 4 < len(floor)
                and x + 4 < len(floor[0])
                and floor[y - 4][x - 4] == "X"
                and floor[y - 3][x - 3] == "X"
                and floor[y - 2][x - 2] == "X"
                and floor[y - 1][x - 1] == "X"
                and floor[y + 4][x + 4] == "X"
                and floor[y + 3][x + 3] == "X"
                and floor[y + 2][x + 2] == "X"
                and floor[y + 1][x + 1] == "X"
            ):
                found = True
                should_print = True
                print("\n".join(["".join(row) for row in floor]))

    if should_print:
        print("=" * 20 + " " + str(i + 1))


def loop(initial_robots: Robots, w: int, h: int, times: int) -> Robots:
    robots = initial_robots
    for i in range(times):
        robots = tick(robots, w, h)
        draw(robots, w, h, i)
    return robots


def count_robots(robots: Robots, w: int, h: int) -> tuple[int, int, int, int]:
    q1, q2, q3, q4 = 0, 0, 0, 0
    for (px, py), _ in robots:
        if px == w // 2 or py == h // 2:
            continue
        if px < w // 2:
            if py < h // 2:
                q1 += 1
            else:
                q3 += 1
        else:
            if py < h // 2:
                q2 += 1
            else:
                q4 += 1
    return (q1, q2, q3, q4)


def get_safety_factor(robot_counts: tuple[int, int, int, int]) -> int:
    return reduce(lambda acc, n: acc * n, list(robot_counts))


def run(data: str, part_2: bool = False):
    w = 11 if os.getenv("TEST") else 101
    h = 7 if os.getenv("TEST") else 103
    print(w)
    robots = parse_robots(data)
    new_position = loop(robots, w, h, 100000000)
    robot_counts = count_robots(new_position, w, h)
    return get_safety_factor(robot_counts)
