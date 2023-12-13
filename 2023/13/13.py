import math
import tqdm
import itertools
import os, sys, inspect
currdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
maindir = os.path.dirname(os.path.dirname(currdir))
sys.path.append(maindir)
from utils import advent

advent.setup(2023, 13)

DEBUG = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""

def find_mirror(patterns, horizontal):
    tot = 0
    indexes = [0]*len(patterns)
    for n, p in enumerate(patterns):
        for i in range(len(p) - 1):
            if p[i] == p[i+1]:
                dx = i + 1
                sx = i
                while sx > 0 and dx < len(p) - 1:
                    sx -= 1
                    dx += 1
                    if p[sx] != p[dx]:
                        sx += 1
                        dx -= 1
                        break
                if sx == 0 or dx == len(p) - 1:
                    if horizontal:
                        tot += (i+1)*100
                        indexes[n] = (i, 'h')
                    else:
                        tot += i+1
                        indexes[n] = (i, 'v')
                    break
    return tot, indexes

def find_and_fix_smudge_v2(pattern, reflection_index, horizontal):
    def flip_char(char):
        return '.' if char == '#' else '#'

    if horizontal:
        # Reflection line is horizontal, check rows
        for i in range(reflection_index):
            mirrored_row = len(pattern) - 1 - i
            for j in range(len(pattern[i])):
                if pattern[i][j] != pattern[mirrored_row][j]:
                    # Found the smudge, fix it
                    pattern[mirrored_row] = pattern[mirrored_row][:j] + flip_char(pattern[mirrored_row][j]) + pattern[mirrored_row][j+1:]
                    return pattern
    else:
        # Reflection line is vertical, check columns
        for i in range(len(pattern)):
            for j in range(reflection_index):
                mirrored_column = len(pattern[i]) - 1 - j
                if pattern[i][j] != pattern[i][mirrored_column]:
                    # Found the smudge, fix it
                    pattern[i] = pattern[i][:mirrored_column] + flip_char(pattern[i][mirrored_column]) + pattern[i][mirrored_column+1:]
                    return pattern
    return pattern  # No smudge found or pattern already correct


def find_mirror2(patterns, horizontal, indexes):
    hv = {True: 'h', False: 'v'}
    tot = 0
    remaining = []
    for n, p in enumerate(patterns):
        done = False
        for i in range(len(p) - 1):
            if [p[i][k] == p[i+1][k] for k in range(len(p[i]))].count(True) == len(p[i]) - 1 and not done:
                #è come se avessi cambiato un elemento delle due righe adiacenti
                done = True
                dx = i + 1
                sx = i
                while sx > 0 and dx < len(p) - 1 and indexes[n] != (i, hv[horizontal]):
                    sx -= 1
                    dx += 1
                    if p[sx] != p[dx]:
                        sx += 1
                        dx -= 1
                        break
                if sx == 0 or dx == len(p) - 1:
                    if horizontal:
                        tot += (i+1)*100
                    else:
                        tot += i+1
                    break
            elif p[i] == p[i+1]:
                dx = i + 1
                sx = i
                while sx > 0 and dx < len(p) - 1:
                    sx -= 1
                    dx += 1
                    if [p[sx][k] == p[dx][k] for k in range(len(p[sx]))].count(True) == len(p[sx]) - 1 and not done and indexes[n] != (i, hv[horizontal]):
                        done = True
                        p[sx] = p[dx]
                    if p[sx] != p[dx]:
                        sx += 1
                        dx -= 1
                        break
                if (sx == 0 or dx == len(p) - 1) and done:
                    if horizontal:
                        tot += (i+1)*100
                    else:
                        tot += i+1
                    break
        if not done:
            remaining.append(p)
    return tot, remaining


def part1(data: str) -> int:
    patterns = data.split("\n\n")
    patterns = [x.splitlines() for x in patterns]

    tot = 0    
    #search horizontal mirror:
    ans, indexes = find_mirror(patterns, True)
    tot += ans

    #search vertical mirror:
    transposed = [list(map(list, zip(*p))) for p in patterns]
    transposed_patterns = []
    for matrix in transposed:
        matrix = [''.join(x) for x in matrix]
        transposed_patterns.append(matrix)
    
    ans, indexes = find_mirror(transposed_patterns, False)
    tot += ans
    return tot, indexes

def part2(data: str, indexes) -> int:
    patterns = data.split("\n\n")
    patterns = [x.splitlines() for x in patterns]
    
    #search horizontal mirror:
    tot, remaining = find_mirror2(patterns, True, indexes)

    #search vertical mirror:
    transposed = [list(map(list, zip(*p))) for p in remaining]
    transposed_patterns = []
    for matrix in transposed:
        matrix = [''.join(x) for x in matrix]
        transposed_patterns.append(matrix)
    toadd, _ = find_mirror2(transposed_patterns, False, indexes)
    return tot+toadd

if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read()
    ans1, indexes1 = part1(DEBUG)
    print(ans1)
    ans1b, indexes1b = part1(data)
    print(ans1b)

    #advent.print_answer(1, part1(data))
    print(part2(DEBUG, indexes1))
    advent.print_answer(2, part2(data, indexes1b))