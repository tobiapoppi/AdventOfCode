from utils import advent
from tqdm import tqdm
advent.setup(2024, 9)

DEBUG = """2333133121414131402"""


def make_list(data):
    l = []
    c = 0
    for i, n in enumerate(data):
        if i % 2 == 0:
            for _ in range(n):
                l.append(c)
            c += 1
        else:
            for _ in range(n):
                l.append(".")
    return l


def part1(data):
    data = data.strip().replace("\n", "")
    data = [int(x) for x in data]
    l = make_list(data)

    right = len(l) - 1
    new_l = []
    count_digits = 0
    for i in l:
        if i != ".":
            count_digits += 1
    for i in range(count_digits):
        if str(l[i]) != ".":
            new_l.append(l[i])
        else:
            while l[right] == ".":
                right -= 1
            new_l.append(l[right])
            right -= 1

    s = sum([int(n) * i for i, n in enumerate(new_l)])
    return s


def part2(data):
    data = data.strip().replace("\n", "")
    data = [int(x) for x in data]
    l = make_list(data)

    num_ranges = []
    dot_ranges = []
    i = 0
    while i < len(l):
        n = l[i]
        if n == ".":
            c = 1
            while i + c < len(l) and l[i + c] == ".":
                c += 1
            dot_ranges.append((i, i + c))
        else:
            c = 1
            while i + c < len(l) and l[i + c] == n:
                c += 1
            num_ranges.append((i, i + c))
        i += c

    for r in tqdm(num_ranges[::-1]):
        start, end = r
        length = end - start
        for ir, dr in enumerate(dot_ranges):
            dstart, dend = dr
            dlength = dend - dstart
            if dlength >= length and dstart < start:
                for i in range(length):
                    l[dstart + i], l[start + i] = l[start + i], "."
                if dlength > length:
                    dot_ranges[ir] = (dstart + length, dend)
                elif dlength == length:
                    dot_ranges.pop(ir)
                break

    s = sum([int(n) * i for i, n in enumerate(l) if n != "."])
    return s


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read()
    print(part1(DEBUG))
    advent.print_answer(1, part1(data))
    print(part2(DEBUG))
    advent.print_answer(2, part2(data))
