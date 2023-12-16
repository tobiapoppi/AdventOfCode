import math
import tqdm
import itertools
import os
import sys
import inspect
from collections import deque
currdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
maindir = os.path.dirname(os.path.dirname(currdir))
sys.path.append(maindir)
from utils import advent

advent.setup(2023, 16)

DEBUG = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|...."""


def trace_beams(lines, start=(0, 0), start_dir=(0, 1)):
    first = True
    pos = start
    direction = start_dir
    full_hist = set()
    energized = [[0] * len(lines[0]) for _ in range(len(lines))]
    coda = deque()
    while coda or first:
        if first:
            first = False
            newpos = (pos[0], pos[1])
            dir_r, dir_c = direction
            energized[newpos[0]][newpos[1]] = 1

        else:
            r, c, dir_r, dir_c = coda.popleft()
            if (r, c, dir_r, dir_c) in full_hist:
                continue
            full_hist.add((r, c, dir_r, dir_c))
            energized[r][c] = 1

            newpos = (r + dir_r, c + dir_c)

            if not -1 < newpos[0] < len(lines) or not -1 < newpos[1] < len(lines[0]):
                continue

        if lines[newpos[0]][newpos[1]] == '|' and dir_r == 0:  # moving horizontally, need to split
            new_directions = [(1, 0), (-1, 0)]
            coda.extend((newpos[0], newpos[1], dr, dc) for dr, dc in new_directions)

        elif lines[newpos[0]][newpos[1]] == '-' and dir_c == 0:  # moving vertically, need to split
            new_directions = [(0, 1), (0, -1)]
            coda.extend((newpos[0], newpos[1], dr, dc) for dr, dc in new_directions)

        elif lines[newpos[0]][newpos[1]] == '/':
            if (dir_r, dir_c) == (0, 1):
                coda.append((newpos[0], newpos[1], -1, 0))
            elif (dir_r, dir_c) == (1, 0):
                coda.append((newpos[0], newpos[1], 0, -1))
            elif (dir_r, dir_c) == (0, -1):
                coda.append((newpos[0], newpos[1], 1, 0))
            else:
                coda.append((newpos[0], newpos[1], 0, 1))

        elif lines[newpos[0]][newpos[1]] == '\\':
            if (dir_r, dir_c) == (0, 1):
                coda.append((newpos[0], newpos[1], 1, 0))
            elif (dir_r, dir_c) == (1, 0):
                coda.append((newpos[0], newpos[1], 0, 1))
            elif (dir_r, dir_c) == (0, -1):
                coda.append((newpos[0], newpos[1], -1, 0))
            else:
                coda.append((newpos[0], newpos[1], 0, -1))

        else:
            coda.append((newpos[0], newpos[1], dir_r, dir_c))
    return energized


def part1(lines: list[str]) -> int:
    energized = trace_beams(lines)
    tot = sum([l.count(1) for l in energized])
    return tot


def part2(data: list[str]) -> int:
    angles = [(0, 0), (0, len(data[0]) - 1), (len(data) - 1, 0), (len(data) - 1, len(data[0]) - 1)]
    dirs = [[(0, 1), (1, 0)], [(0, -1), (1, 0)], [(0, 1), (-1, 0)], [(0, -1), (-1, 0)]]
    energized_list = [trace_beams(data, start, direction)
                      for start, directions in zip(angles, dirs) for direction in directions]
    tot = [sum([l.count(1) for l in energized]) for energized in energized_list]
    return max(tot)


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read()
    print(part1(DEBUG.splitlines()))
    advent.print_answer(1, part1(data.splitlines()))
    print(part2(DEBUG.splitlines()))
    advent.print_answer(2, part2(data.splitlines()))
