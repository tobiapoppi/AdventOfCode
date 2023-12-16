import math
import tqdm
import itertools
import os
import sys
import inspect
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


def trace_beams(lines, start=(0, 0), direction=(0, 1), energized_last={}, full_hist=[]):
    pos = start  # riga, colonna
    full_hist = full_hist
    direction = direction
    energized = [[0] * len(lines[0]) for _ in range(len(lines))]
    if energized_last != {}:
        for i in range(len(lines)):
            for j in range(len(lines[0])):
                if energized_last[i][j] == 1:
                    energized[i][j] = 1
    first = True

    while True:
        if first:
            first = False
            newpos = (pos[0], pos[1])
        else:
            newpos = (pos[0] + direction[0], pos[1] + direction[1])
        if newpos[0] < 0 or newpos[0] >= len(lines) or newpos[1] < 0 or newpos[1] >= len(lines[0]):
            return energized, full_hist

        if lines[newpos[0]][newpos[1]] == '|' and direction[0] == 0:  # moving horizontally, need to split
            direction = [(1, 0), (-1, 0)]
            energized, fh = trace_beams(lines, newpos, direction[0], energized, full_hist)
            full_hist.extend(fh)
            energized, fh = trace_beams(lines, newpos, direction[1], energized, full_hist)
            full_hist.extend(fh)

            return energized, full_hist

        if lines[newpos[0]][newpos[1]] == '-' and direction[1] == 0:  # moving vertically, need to split
            direction = [(0, 1), (0, -1)]
            energized, fh = trace_beams(lines, newpos, direction[0], energized, full_hist)
            full_hist.extend(fh)
            energized, fh = trace_beams(lines, newpos, direction[1], energized, full_hist)
            full_hist.extend(fh)

            return energized, full_hist

        if lines[newpos[0]][newpos[1]] == '/':
            if direction == (0, 1):
                direction = (-1, 0)
            elif direction == (1, 0):
                direction = (0, -1)
            elif direction == (0, -1):
                direction = (1, 0)
            else:
                direction = (0, 1)

        if lines[newpos[0]][newpos[1]] == '\\':
            if direction == (0, 1):
                direction = (1, 0)
            elif direction == (1, 0):
                direction = (0, 1)
            elif direction == (0, -1):
                direction = (-1, 0)
            else:
                direction = (0, -1)

        pos = newpos
        energized[newpos[0]][newpos[1]] = 1
        if (newpos[0], newpos[1], direction[0], direction[1]) in full_hist:
            return energized, full_hist
        full_hist.append((newpos[0], newpos[1], direction[0], direction[1]))


def part1(lines: list[str]) -> int:
    energized, _ = trace_beams(lines)
    tot = sum([l.count(1) for l in energized])
    return tot


def part2(data: list[str]) -> int:
    return


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read()
    print(part1(DEBUG.splitlines()))
    advent.print_answer(1, part1(data.splitlines()))
    # print(part2(DEBUG.splitlines()))
    # advent.print_answer(2, part2(data.splitlines()))
