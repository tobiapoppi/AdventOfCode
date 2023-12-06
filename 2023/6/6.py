import math
import tqdm
import os, sys, inspect
currdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
maindir = os.path.dirname(os.path.dirname(currdir))
sys.path.append(maindir)
from utils import advent

advent.setup(2023, 6)

DEBUG = """Time:      7  15   30
Distance:  9  40  200"""

def part1(data: list[str]) -> int:
    times = list(map(int, data[0].split(':')[1].split()))
    distances = list(map(int,data[1].split(':')[1].split()))
    ways_to_win = [sum([(t-i)*i > d for i in range(t+1)]) for t, d in zip(times, distances)]
    return math.prod(ways_to_win)

def part2(data: list[str]) -> int:
    ways = 0
    times = int(data[0].split(':')[1].replace(' ', ''))
    distances = int(data[1].split(':')[1].replace(' ', ''))
    ways = sum([(times-i) * i > distances for i in tqdm.tqdm(range(times+1))])
    return ways

if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read()
    print(part1(DEBUG.splitlines()))
    advent.print_answer(1, part1(data.splitlines()))
    print(part2(DEBUG.splitlines()))
    advent.print_answer(2, part2(data.splitlines()))