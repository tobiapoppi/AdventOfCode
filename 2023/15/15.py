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

advent.setup(2023, 15)

DEBUG = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""


def HASH(s):
    curr_val = 0
    for c in s:
        # add to curr_val the ascii value of c
        curr_val += ord(c)
        curr_val *= 17
        curr_val = curr_val % 256
    return curr_val


def part1(data) -> int:
    data = data.replace('\n', '')
    data = data.split(',')
    tot = 0
    for d in data:
        tot += HASH(d)
    return tot


def part2(data: list[str]) -> int:
    data = data.replace('\n', '')
    data = data.split(',')
    boxes = [{} for _ in range(256)]
    for d in data:
        # fl must be an int
        label, fl = d.split('=') if '=' in d else (d[:-1], 0)
        fl = int(fl)
        nbox = HASH(label)

        if fl == 0 and label in boxes[nbox]:
            del boxes[nbox][label]

        elif fl != 0:
            boxes[nbox][label] = fl

    tot = 0
    for i, box in enumerate(boxes):
        for k, fl in enumerate(box.values()):
            tot += (i + 1) * (k + 1) * fl
    return tot


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read()
    print(part1(DEBUG))
    advent.print_answer(1, part1(data))
    print(part2(DEBUG))
    advent.print_answer(2, part2(data))
