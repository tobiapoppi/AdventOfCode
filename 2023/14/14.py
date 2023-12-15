import hashlib
import inspect
import math
import os
import sys
from functools import partial

import tqdm


currdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
maindir = os.path.dirname(os.path.dirname(currdir))
sys.path.append(maindir)

from utils import advent
advent.setup(2023, 14)

DEBUG = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""


def calc_score(data):
    lines = data
    columns = [''.join([line[i] for line in lines]) for i in range(len(lines[0]))]
    tot = 0
    for i, col in enumerate(columns[::-1]):
        tot += col.count('O') * i
    return tot


def get_lines(data):
    lines = data
    columns = [''.join([line[i] for line in lines]) for i in range(len(lines[0]))]
    splitted = c.split('#')
        for i, s in enumerate(splitted):
            n_rounded_rocks = [ch == 'O' for ch in s].count(True)
            splitted[i] = 'O'*n_rounded_rocks + '.'*(len(s) - n_rounded_rocks)
        columns[n] = '#'.join(splitted)
    # for n, c in enumerate(columns):
    #     columns = '#'.join((map(''.join, list(map(partial(sorted, reverse=True), c.split('#'))))))

    lines = [''.join([col[i] for col in columns])
             for i in range(len(columns[0]))]
    return lines


def rotate_strings_clockwise(strings):
    matrix = [list(row) for row in strings]
    transposed_matrix = list(zip(*matrix))
    return ["".join(reversed(row)) for row in transposed_matrix]


def part1(data: list[str]) -> int:
    return get_lines(data, True)[0]


def part2(data: list[str]) -> int:
    tot = 0
    lines = data
    hist = {}

    curr_iter = 0
    done = False
    with tqdm.tqdm(total=1_000_000_000) as pbar:
        while 1:
            curr_iter += 1
            pbar.update(1)

            h = hashlib.sha256(''.join(lines).encode('utf-8')).hexdigest()

            if h in hist and not curr_iter == 1_000_000_000 and not done:
                first_cycle_index = hist[h]
                done = True
                prev_iter = curr_iter
                curr_iter = ((1_000_000_000 - curr_iter) // (curr_iter - first_cycle_index)
                             ) * (curr_iter - first_cycle_index) + first_cycle_index - 1
                pbar.update(curr_iter - prev_iter)

            if curr_iter == 1_000_000_000:
                tot = calc_score(lines)
                break

            for _ in range(4):
                lines = get_lines(lines)
                lines = rotate_strings_clockwise(lines)

            hist[h] = curr_iter

#
    return tot


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read()
    # print(part1(DEBUG.splitlines()))
    # advent.print_answer(1, part1(data.splitlines()))
    print(part2(DEBUG.splitlines()))
    advent.print_answer(2, part2(data.splitlines()))
