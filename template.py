import math
import tqdm
import itertools
import os, sys, inspect
currdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
maindir = os.path.dirname(os.path.dirname(currdir))
sys.path.append(maindir)
from utils import advent

advent.setup(year, day)

DEBUG = """
"""

def part1(data: list[str]) -> int:
    return

def part2(data: list[str]) -> int:
    return 

if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read()
    print(part1(DEBUG.splitlines()))
    advent.print_answer(1, part1(data.splitlines()))
    #print(part2(DEBUG.splitlines()))
    #advent.print_answer(2, part2(data.splitlines()))