import math
import tqdm
import itertools
import os, sys, inspect
currdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
maindir = os.path.dirname(os.path.dirname(currdir))
sys.path.append(maindir)
from utils import advent

advent.setup(2023, 9)

DEBUG = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

def part1(data: list[str]) -> int:
    lines = [list(map(int, x.split())) for x in data]
    total = 0
    for l in lines:
        graph = [l]
        while not all(l[x] == 0 for x in range(len(l))):
            diff = []
            for i in range(len(l)-1):
                diff.append(l[i+1] - l[i])
            graph.append(diff)
            l = diff
        
        x = [0]
        for r in range(len(graph)-1, -1, -1):
            x.append(graph[r-1][-1] + x[-1])
        total += x[-1]
    return total

def part2(data: list[str]) -> int:
    lines = [list(map(int, x.split())) for x in data]
    total = 0
    for l in lines:
        graph = [l]
        while not all(l[x] == 0 for x in range(len(l))):
            diff = []
            for i in range(len(l)-1):
                diff.append(l[i+1] - l[i])
            graph.append(diff)
            l = diff
        
        x = [0]
        for r in range(len(graph)-1, 0, -1):
            x.append(graph[r-1][0] - x[-1])
        total += x[-1]
    return total 

if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read()
    print(part1(DEBUG.splitlines()))
    advent.print_answer(1, part1(data.splitlines()))
    print(part2(DEBUG.splitlines()))
    advent.print_answer(2, part2(data.splitlines()))