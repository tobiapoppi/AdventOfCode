from collections import defaultdict
from utils import advent
advent.setup(2024, 5)

DEBUG = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""


def is_correct(r, pages_before):
    if len(r) % 2 == 0:
        return False
    for i, a in enumerate(r):
        for j, b in enumerate(r):
            if i < j and a not in pages_before[b]:
                return False
    return True


def prepare_data(data):
    input_rules, input_records = data.strip().split('\n\n')
    input_rules = input_rules.split('\n')
    input_records = input_records.split('\n')
    pages_before = defaultdict(set)

    rules = [[int(el) for el in x.split('|')] for x in input_rules]
    for a, b in rules:
        pages_before[b].add(a)

    records = [[int(el) for el in x.split(',')] for x in input_records]
    return pages_before, records


def part1(data):
    pages_before, records = prepare_data(data)
    out = 0
    for r in records:
        corr = is_correct(r, pages_before)
        if corr:
            out += r[len(r) // 2]
    return out


def part2(data):
    pages_before, records = prepare_data(data)
    out = 0
    for r in records:
        corr = is_correct(r, pages_before)
        if corr:
            continue
        ordered = []
        how_many_before = {n: len(pages_before[n] & set(r)) for n in r}
        while len(ordered) < len(r):
            for k, v in how_many_before.items():
                if v == 0 and k not in ordered:
                    ordered.append(k)
                    for n in r:
                        if n != k and k in pages_before[n]:
                            how_many_before[n] -= 1

        out += ordered[len(r) // 2]
    return out


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read()
    print(part1(DEBUG))
    advent.print_answer(1, part1(data))
    print(part2(DEBUG))
    advent.print_answer(2, part2(data))
