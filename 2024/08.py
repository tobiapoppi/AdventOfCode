from utils import advent
advent.setup(2024, 8)

DEBUG = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""


def get_nodes(data):
    nodes = {}
    for i, row in enumerate(data):
        for j, cell in enumerate(row):
            if cell != ".":
                if cell not in nodes:
                    nodes[cell] = []
                nodes[cell].append((i, j))
    return nodes


def find_antinodes(data, a, b):
    anti = set()
    diff = (a[0] - b[0], a[1] - b[1])
    antinode_a = (a[0] + diff[0], a[1] + diff[1])
    antinode_b = (b[0] - diff[0], b[1] - diff[1])
    if 0 <= antinode_a[0] < len(data) and 0 <= antinode_a[1] < len(data[0]):
        anti.add(antinode_a)
    if 0 <= antinode_b[0] < len(data) and 0 <= antinode_b[1] < len(data[0]):
        anti.add(antinode_b)
    return anti


def find_antinodes_2(data, a, b):
    anti = set()
    anti.add(a)
    anti.add(b)
    diff = (a[0] - b[0], a[1] - b[1])
    antinode_a = (a[0] + diff[0], a[1] + diff[1])
    while 0 <= antinode_a[0] < len(data) and 0 <= antinode_a[1] < len(data[0]):
        anti.add(antinode_a)
        a = antinode_a
        antinode_a = (a[0] + diff[0], a[1] + diff[1])
    antinode_b = (b[0] - diff[0], b[1] - diff[1])
    while 0 <= antinode_b[0] < len(data) and 0 <= antinode_b[1] < len(data[0]):
        anti.add(antinode_b)
        b = antinode_b
        antinode_b = (b[0] - diff[0], b[1] - diff[1])
    return anti


def part1(data):
    data = data.strip().split("\n")
    data = [list(line) for line in data]
    nodes = get_nodes(data)
    antinodes = set()
    for _, vals in nodes.items():
        if len(vals) == 1:
            continue
        for i in range(len(vals)):
            for j in range(i + 1, len(vals)):
                a = (vals[i][0], vals[i][1])
                b = (vals[j][0], vals[j][1])
                anti = find_antinodes(data, a, b)
                antinodes.update(anti)
    return len(antinodes)


def part2(data):
    data = data.strip().split("\n")
    data = [list(line) for line in data]
    nodes = get_nodes(data)
    antinodes = set()
    for _, vals in nodes.items():
        if len(vals) == 1:
            continue
        for i in range(len(vals)):
            for j in range(i + 1, len(vals)):
                a = (vals[i][0], vals[i][1])
                b = (vals[j][0], vals[j][1])
                anti = find_antinodes_2(data, a, b)
                antinodes.update(anti)
    return len(antinodes)


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read()
    print(part1(DEBUG))
    advent.print_answer(1, part1(data))
    print(part2(DEBUG))
    advent.print_answer(2, part2(data))
