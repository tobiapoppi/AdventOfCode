from utils import advent
advent.setup(2024, 10)

DEBUG = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""


def dfs(data, x, y, visited, global_visited):
    if (x, y) in visited:
        return 0
    if data[x][y] == 9:
        if global_visited:
            visited.add((x, y))
        return 1

    visited.add((x, y))
    total_score = 0

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dx, dy in dirs:
        xnew, ynew = x + dx, y + dy

        if 0 <= xnew < len(data) and 0 <= ynew < len(data[0]) and data[xnew][ynew] == data[x][y] + 1:
            total_score += dfs(data, xnew, ynew, visited, global_visited)

    if not global_visited:
        visited.remove((x, y))
    return total_score


def part1(data):
    data = data.strip().split("\n")
    data = [[int(x) for x in row] for row in data]
    scores = 0

    for x in range(len(data)):
        for y in range(len(data[x])):
            if data[x][y] == 0:
                scores += dfs(data, x, y, set(), True)
    return scores


def part2(data):
    data = data.strip().split("\n")
    data = [[int(x) for x in row] for row in data]
    scores = 0

    for x in range(len(data)):
        for y in range(len(data[x])):
            if data[x][y] == 0:
                scores += dfs(data, x, y, set(), False)
    return scores


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read()
    print(part1(DEBUG))
    advent.print_answer(1, part1(data))
    print(part2(DEBUG))
    advent.print_answer(2, part2(data))
