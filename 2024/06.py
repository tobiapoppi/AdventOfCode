from utils import advent
advent.setup(2024, 6)

DEBUG = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""


def prepare_data(data):
    map = data.strip().split("\n")
    map = [list(line) for line in map]
    return map


def check_loop(map, pos, dir):
    visited_dir = set()
    while True:
        visited_dir.add((pos[0], pos[1], dir[0], dir[1]))
        if not 0 <= pos[0] + dir[0] < len(map) or not 0 <= pos[1] + dir[1] < len(map[0]):
            return False
        if map[pos[0] + dir[0]][pos[1] + dir[1]] == "#":
            if dir == (0, 1):
                dir = (1, 0)
            elif dir == (1, 0):
                dir = (0, -1)
            elif dir == (0, -1):
                dir = (-1, 0)
            elif dir == (-1, 0):
                dir = (0, 1)
        else:
            pos = (pos[0] + dir[0], pos[1] + dir[1])
        if (pos[0], pos[1], dir[0], dir[1]) in visited_dir:
            return True


def find_start(map):
    for i, row in enumerate(map):
        for j, cell in enumerate(row):
            if cell in "^v<>":
                pos = (i, j)
                dir = (0, 1) if cell == ">" else (0, -1) if cell == "<" else (1, 0) if cell == "v" else (-1, 0)
                return pos, dir


def all_visited(map, pos, dir):
    visited = set()
    visited.add(pos)
    while True:
        if not 0 <= pos[0] + dir[0] < len(map) or not 0 <= pos[1] + dir[1] < len(map[0]):
            break
        if map[pos[0] + dir[0]][pos[1] + dir[1]] == "#":
            if dir == (0, 1):
                dir = (1, 0)
            elif dir == (1, 0):
                dir = (0, -1)
            elif dir == (0, -1):
                dir = (-1, 0)
            elif dir == (-1, 0):
                dir = (0, 1)
        else:
            pos = (pos[0] + dir[0], pos[1] + dir[1])
            visited.add(pos)
    return visited


def part1(data):
    map = prepare_data(data)
    pos, dir = find_start(map)
    visited = all_visited(map, pos, dir)
    return len(visited)


def part2(data):
    map = prepare_data(data)
    pos, dir = find_start(map)
    visited = all_visited(map, pos, dir)
    loops = 0
    for i, j in visited:
        if map[i][j] == ".":
            map[i][j] = "#"
            if check_loop(map, pos, dir):
                loops += 1
            map[i][j] = "."
    return loops


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read()
    print(part1(DEBUG))
    advent.print_answer(1, part1(data))
    print(part2(DEBUG))
    advent.print_answer(2, part2(data))
