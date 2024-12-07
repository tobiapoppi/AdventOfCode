from utils import advent
advent.setup(2024, 7)

DEBUG = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""


def part1(data):
    data = data.strip().split("\n")
    sum = 0
    for line in data:
        key = int(line.split(":")[0])
        val = line.split(":")[1].strip().split(" ")
        r = set()
        r.add(int(val[0]))
        for i in range(1, len(val)):
            a = [x + int(val[i]) for x in r]
            b = [x * int(val[i]) for x in r]
            r = set(a + b)
        if key in r:
            sum += key
    return sum


def part2(data):
    data = data.strip().split("\n")
    sum = 0
    for line in data:
        key = int(line.split(":")[0])
        val = line.split(":")[1].strip().split(" ")
        r = set()
        r.add(int(val[0]))
        for i in range(1, len(val)):
            a = [x + int(val[i]) for x in r]
            b = [x * int(val[i]) for x in r]
            c = [int(str(x) + str(val[i])) for x in r]
            r = set(a + b + c)
        if key in r:
            sum += key
    return sum


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read()
    print(part1(DEBUG))
    advent.print_answer(1, part1(data))
    print(part2(DEBUG))
    advent.print_answer(2, part2(data))
