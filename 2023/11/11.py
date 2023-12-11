import math
import tqdm
import itertools
import os, sys, inspect
currdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
maindir = os.path.dirname(os.path.dirname(currdir))
sys.path.append(maindir)
from utils import advent
import copy

advent.setup(2023, 11)

DEBUG = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

def part1(data: list[str]) -> int:
    grid = [list(x) for x in data]
    expanded_grid = []
    for r in range(len(grid)):
        if all(c == '.' for c in grid[r]):
            expanded_grid.append(['.'] * len(grid[r]))
            expanded_grid.append(['.'] * len(grid[r]))
            continue
        expanded_grid.append(grid[r].copy())
    
    new_expanded_grid = copy.deepcopy(expanded_grid)
    n_expanded_cols = 0
    for c in range(len(expanded_grid[0])):
        if all(expanded_grid[r][c] == '.' for r in range(len(expanded_grid))):
            #add a column full of dots
            for r in range(len(expanded_grid)):
                new_expanded_grid[r].insert(c + n_expanded_cols, '.')
            n_expanded_cols += 1
            continue
    expanded_grid = new_expanded_grid.copy()
    
    galaxies = {}
    count = 0
    for r in range(len(expanded_grid)):
        for c in range(len(expanded_grid[r])):
            if expanded_grid[r][c] == '#':
                count += 1
                galaxies[count] = (r, c)
                expanded_grid[r][c] = count

    pairs = list(itertools.combinations(range(1, count + 1), 2))
    distances = []
    for p in pairs:
        p1 = galaxies[p[0]]
        p2 = galaxies[p[1]]
        if p1[0] == p2[0]:
            #same row
            distances.append(abs(p1[1] - p2[1]))
        elif p1[1] == p2[1]:
            #same column
            distances.append(abs(p1[0] - p2[0]))
        else:
            #distance from pixels
            distances.append(abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]))
    return sum(distances)

def part2(data: list[str]) -> int:
    grid = [list(x) for x in data]
    vertical_expansions = []
    horizontal_expansions = []
    for r in range(len(grid)):
        if all(c == '.' for c in grid[r]):
            vertical_expansions.append(r)
            continue
    
    for c in range(len(grid[0])):
        if all(grid[r][c] == '.' for r in range(len(grid))):
            #add a column full of dots
            horizontal_expansions.append(c)
            continue
    
    galaxies = {}
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == '#':
                count += 1
                galaxies[count] = (r, c)
                grid[r][c] = count

    pairs = list(itertools.combinations(range(1, count + 1), 2))
    distances = []
    expansion_factor = 1_000_000
    for p in pairs:
        p1 = galaxies[p[0]]
        p2 = galaxies[p[1]]

        # Count expansions between galaxies
        n_vert_expansion = sum(v in range(min(p1[0], p2[0]), max(p1[0], p2[0])) for v in vertical_expansions)
        n_horiz_expansion = sum(h in range(min(p1[1], p2[1]), max(p1[1], p2[1])) for h in horizontal_expansions)

        # Calculate distance
        distance = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        distance += n_vert_expansion * (expansion_factor - 1) + n_horiz_expansion * (expansion_factor - 1)
        distances.append(distance)

    return sum(distances)

if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read()
    print(part1(DEBUG.splitlines()))
    advent.print_answer(1, part1(data.splitlines()))
    print(part2(DEBUG.splitlines()))
    advent.print_answer(2, part2(data.splitlines()))