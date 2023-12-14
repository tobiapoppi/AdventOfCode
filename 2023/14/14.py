import math
import tqdm
import itertools
import os, sys, inspect
currdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
maindir = os.path.dirname(os.path.dirname(currdir))
sys.path.append(maindir)
from utils import advent

advent.setup(2023, 14)

DEBUG = """OOOO.#.O..
OO..#....#
OO..O##..O
O..#.OO...
........#.
..#....#.#
..O..#.O.O
..O.......
#....###..
#....#...."""

def get_lines(data, withcalc=False):
    lines = data
    columns = [''.join([line[i] for line in lines]) for i in range(len(lines[0]))]
    
    for n, c in enumerate(columns):
        splitted = c.split('#')
        for i, s in enumerate(splitted):
            n_rounded_rocks = [ch == 'O' for ch in s].count(True)
            splitted[i] = 'O'*n_rounded_rocks + '.'*(len(s) - n_rounded_rocks)
        columns[n] = '#'.join(splitted)
    
    tot = 0
    if withcalc:
        for col in columns:
            for i, c in enumerate(col):
                if c == 'O':
                    tot += len(col) - i
        
    lines = [''.join([col[i] for col in columns]) for i in range(len(columns[0]))]
    return tot, lines

def rotate_strings_clockwise(strings):
    # Convert the list of strings to a list of list of characters
    matrix = [list(row) for row in strings]

    transposed_matrix = list(zip(*matrix))

    return ["".join(reversed(row)) for row in transposed_matrix]

def part1(data: list[str]) -> int:
    return get_lines(data, True)[0]    


def part2(data: list[str]) -> int:
    tot = 0
    lines = data

    tot, lines = get_lines(lines)
    for k in range(3):
        lines = rotate_strings_clockwise(lines)
        tot, lines = get_lines(lines)

    for i in range(999_999_998):
        for k in range(4):
            lines = rotate_strings_clockwise(lines)
            tot, lines = get_lines(lines)

    for k in range(3):
        lines = rotate_strings_clockwise(lines)
        tot, lines = get_lines(lines)
    lines = rotate_strings_clockwise(lines)
    tot, lines = get_lines(lines, True)

    return tot

if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read()
    print(part1(DEBUG.splitlines()))
    advent.print_answer(1, part1(data.splitlines()))
    print(part2(DEBUG.splitlines()))
    advent.print_answer(2, part2(data.splitlines()))