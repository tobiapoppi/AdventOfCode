import math
import tqdm
import itertools
from functools import cache
import os, sys, inspect
currdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
maindir = os.path.dirname(os.path.dirname(currdir))
sys.path.append(maindir)
from utils import advent

advent.setup(2023, 12)

DEBUG = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

@cache
def count_solutions(pattern, group_sizes, in_group=0):
    if not pattern:
        return not group_sizes and in_group == 0

    solutions = 0
    choices = ['.', '#'] if pattern[0] == '?' else [pattern[0]]
    for choice in choices:
        if choice == '#':
            solutions += count_solutions(pattern[1:], group_sizes, in_group + 1)
        else:
            if in_group > 0:
                if group_sizes and group_sizes[0] == in_group:
                    solutions += count_solutions(pattern[1:], group_sizes[1:])
            else:
                solutions += count_solutions(pattern[1:], group_sizes)
    return solutions

def part1(data: list[str]) -> int:
    lines = [x.split() for x in data]
    lines = [(pattern, tuple(map(int, sizes.split(",")))) for pattern, sizes in lines]
    tot = sum(count_solutions(pattern + ".", sizes) for pattern, sizes in lines)
    return tot
    

def part2(data: list[str]) -> int:
    lines = [x.split() for x in data]
    lines = [('?'.join([pattern] * 5), tuple(map(int, sizes.split(","))) * 5) for pattern, sizes in lines]
    tot = sum(count_solutions(pattern + ".", sizes) for pattern, sizes in lines)
    return tot

if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read()
    print(part1(DEBUG.splitlines()))
    advent.print_answer(1, part1(data.splitlines()))
    print(part2(DEBUG.splitlines()))
    advent.print_answer(2, part2(data.splitlines()))