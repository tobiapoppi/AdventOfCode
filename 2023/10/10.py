import math
import tqdm
import itertools
import os, sys, inspect
currdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
maindir = os.path.dirname(os.path.dirname(currdir))
sys.path.append(maindir)
from utils import advent

advent.setup(2023, 10)

DEBUG = """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ..."""

#spostamenti, direzione futura
commands = {'|': [[(0, -1), (0, -1)], [(0, 1), (0, 1)]],
            '-': [[(1, 0), (1, 0)], [(-1, 0), (-1, 0)]],
            'L': [[(0, -1), (1, 0)], [(-1, 0), (0, 1)]],
            'J': [[(0, -1), (-1, 0)], [(1, 0), (0, 1)]],
            'F': [[(-1, 0), (0, -1)], [(0, 1), (1, 0)]],
            '7': [[(1, 0), (0, -1)], [(0, 1), (-1, 0)]],
            'S': [[(0, 0), ['|', '-', 'L', 'J', 'F', '7']]],
            '.': [[(0, 0), ['|', '-', 'L', 'J', 'F', '7']]]}

rot = {(1, 0): 0, (0, 1): 90, (-1, 0): 180, (0, -1): 270}

def part1(data: list[str]) -> int:
    grid = [list(x) for x in data]
    pos = ()
    loop = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'S':
                pos = (x, y)
                break
    nextpos = ()
    loop.append(pos)
    possible_next = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    while nextpos != loop[0]:
        found = False
        for dx in range(pos[0]-1, pos[0]+2):
            for dy in range(pos[1]-1, pos[1]+2):
                if dx < 0 or dy < 0 or dx >= len(grid[0]) or dy >= len(grid):
                    continue
                if (dx, dy) == pos:
                    continue
                if grid[dy][dx] == '.':
                    continue
                if grid[dy][dx] in commands and (dx, dy) not in loop:
                    for c in commands[grid[dy][dx]]:
                        if (dx-pos[0], pos[1]-dy) == c[0] and (dx-pos[0], pos[1]-dy) in possible_next:
                            possible_next = [c[1]]
                            nextpos = (dx, dy)
                            loop.append(nextpos)
                            pos = nextpos
                            found = True
                            break
                if grid[dy][dx] == 'S' and (dx-pos[0], pos[1]-dy) in possible_next:
                    nextpos = (dx, dy)
                    loop.append(nextpos)
                    pos = nextpos
                    found = True
                    break
                if found:
                    break
            if found:
                break

    return len(loop)//2

def part2(data: list[str]) -> int:
    grid = [list(x) for x in data]
    pos = ()
    loop = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'S':
                pos = (x, y)
                break
    nextpos = ()
    loop.append(pos)
    possible_next = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    while nextpos != loop[0]:
        found = False
        for dx in range(pos[0]-1, pos[0]+2):
            for dy in range(pos[1]-1, pos[1]+2):
                if dx < 0 or dy < 0 or dx >= len(grid[0]) or dy >= len(grid):
                    continue
                if (dx, dy) == pos:
                    continue
                if grid[dy][dx] == '.':
                    continue
                if grid[dy][dx] in commands and (dx, dy) not in loop:
                    for c in commands[grid[dy][dx]]:
                        if (dx-pos[0], pos[1]-dy) == c[0] and (dx-pos[0], pos[1]-dy) in possible_next:
                            possible_next = [c[1]]
                            nextpos = (dx, dy)
                            loop.append(nextpos)
                            pos = nextpos
                            found = True
                            break
                if grid[dy][dx] == 'S' and (dx-pos[0], pos[1]-dy) in possible_next:
                    nextpos = (dx, dy)
                    loop.append(nextpos)
                    pos = nextpos
                    found = True
                    break
                if found:
                    break
            if found:
                break
    
    inside = 0
    for y in range(len(grid)):
        cross = 0
        angolo = ''
        for x in range(len(grid[0])):
            if (x, y) in loop:
                if grid[y][x] in ['S', '|']:
                    cross += 1
                elif grid[y][x] == 'J' and angolo == 'F':
                    cross += 1
                elif grid[y][x] == '7' and angolo == 'L':
                    cross += 1
                if grid[y][x] != '-':
                    angolo = grid[y][x]
            else:
                if cross % 2 == 1:
                    inside += 1
    return inside

if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read()
    print(part1(DEBUG.splitlines()))
    advent.print_answer(1, part1(data.splitlines()))
    print(part2(DEBUG.splitlines()))
    advent.print_answer(2, part2(data.splitlines()))