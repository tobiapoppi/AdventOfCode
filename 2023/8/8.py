import math
import tqdm
import itertools
import os, sys, inspect
currdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
maindir = os.path.dirname(os.path.dirname(currdir))
sys.path.append(maindir)
from utils import advent

advent.setup(2023, 8)

DEBUG = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

DEBUG2 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

START = "AAA"
END = "ZZZ"

def part1(data: list[str]) -> int:
    commands = data[0]
    from_ = "AAA"
    lines = [x.split()[0] for x in data[2:]]
    found = False
    steps = 0
    while(1):
        for c in commands:
            steps += 1
            for i, f in enumerate(lines):
                if found:
                    found = False
                    break
                if f == from_:
                    if c == 'L':
                        from_ = data[i+2][7:10]
                        if from_ == "ZZZ":
                            return steps
                        found = True
                        continue
                    else:
                        from_ = data[i+2][12:15]
                        if from_ == "ZZZ":
                            return steps
                        found = True
                        continue
def part2new(data: list[str]) -> int:
    commands = data[0]
    lines = [x.split()[0] for x in data[2:]]
    from_ = [x for x in lines if x[-1] == 'A']
    z_left = [x[7:10] for x in data[2:] if x[7:10][-1] == 'Z']
    z_right = [x[12:15] for x in data[2:] if x[12:15][-1] == 'Z']
    print(1)

def part2(data: list[str]) -> int:
    commands = data[0]
    lines = [x.split()[0] for x in data[2:]]
    from_ = [x for x in lines if x[-1] == 'A']
    found = [False]*len(from_)
    found_z = [False]*len(from_)
    steps_list = []
    steps = 0
    while(1):
        for c in commands:
            if all(found_z):
                return steps
            found_z = [False]*len(from_)
            found = [False]*len(from_)
            steps += 1
            for k, v in enumerate(from_):
                for i, f in enumerate(lines):
                    if f == v:
                        if c == 'L':
                            from_[k] = data[i+2][7:10]
                        else:
                            from_[k] = data[i+2][12:15]
                        
                        if from_[k][-1] == "Z":
                            steps_list.append(steps)
                        found[k] = True
                        break

def part2_improved(data):
    commands = data[0]
    node_map = {line.split(" = ")[0]: line.split(" = ")[1].strip("()").split(", ") for line in data[2:]}

    nodes = [node for node in node_map if node[-1] == 'A']
    steps = 0
    steps_list = []

    while 1:
        new_nodes = []
        for node in nodes:
            next_index = 0 if commands[steps % len(commands)] == 'L' else 1
            next_node = node_map[node][next_index]
            new_nodes.append(next_node)
            if next_node.endswith('Z'):
                steps_list.append(steps + 1)
                print(len(steps_list))
        nodes = new_nodes
        if len(nodes) == len(steps_list): break
        steps += 1
    return math.lcm(*steps_list)

if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read()
    print(part1(DEBUG.splitlines()))
    advent.print_answer(1, part1(data.splitlines()))
    print(part2_improved(DEBUG2.splitlines()))
    advent.print_answer(2, part2_improved(data.splitlines()))