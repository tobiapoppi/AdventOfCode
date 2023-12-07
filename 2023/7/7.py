import math
import tqdm
import itertools
from functools import cmp_to_key
from collections import defaultdict
import os, sys, inspect
currdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
maindir = os.path.dirname(os.path.dirname(currdir))
sys.path.append(maindir)
from utils import advent

advent.setup(2023, 7)

DEBUG = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""
    
def is_greater_than(hand1, hand2, jollys = False):
    order = list('AKQJT98765432')
    if jollys:
        order = list('AKQT98765432J')
    counter = itertools.count()
    values = defaultdict(list)
    for key, value in zip(reversed(order), counter):
        values[key].append(value)
    
    cards_1 = {}
    cards_2 = {}
    c1_jollys = 0
    c2_jollys = 0

    for c1 in hand1:
        if c1 == 'J' and jollys:
            c1_jollys += 1
            continue
        if c1 not in cards_1:
            cards_1[c1] = 0
        cards_1[c1] += 1
    
    for c2 in hand2:
        if c2 == 'J' and jollys:
            c2_jollys += 1
            continue
        if c2 not in cards_2:
            cards_2[c2] = 0
        cards_2[c2] += 1
    
    cards = [cards_1, cards_2]

    if c1_jollys == 5:
        cards[0]['A'] = 5
    if c2_jollys == 5:
        cards[1]['A'] = 5
    for i, r in enumerate([c1_jollys, c2_jollys]):
        if r != 5:
            for _ in range(r):
                maxval = 0
                keymax = ''
                for key,val in cards[i].items():
                    if maxval < val:
                        maxval = val
                        keymax = key
                cards[i][keymax] += 1

    if 5 in cards[0].values() and 5 in cards[1].values():
        count = 0
        while values[hand1[count]] == values[hand2[count]]:
            count += 1
        return 1 if values[hand1[count]] >= values[hand2[count]] else -1
    elif 5 in cards[0].values():
        return 1
    elif 5 in cards[1].values():
        return -1
    
    elif 4 in cards[0].values() and 4 in cards[1].values():
        count = 0
        while values[hand1[count]] == values[hand2[count]]:
            count += 1
        return 1 if values[hand1[count]] >= values[hand2[count]] else -1
    elif 4 in cards[0].values():
        return 1
    elif 4 in cards[1].values():
        return -1

    elif 3 in cards[0].values() and 2 in cards[0].values() and 3 in cards[1].values() and 2 in cards[1].values():
        count = 0
        while values[hand1[count]] == values[hand2[count]]:
            count += 1
        return 1 if values[hand1[count]] >= values[hand2[count]] else -1
    elif 3 in cards[0].values() and 2 in cards[0].values():
        return 1
    elif 3 in cards[1].values() and 2 in cards[1].values():
        return - 1
    
    elif 3 in cards[0].values() and 3 in cards[1].values() :
        count = 0
        while values[hand1[count]] == values[hand2[count]]:
            count += 1
        return 1 if values[hand1[count]] >= values[hand2[count]] else -1
    elif 3 in cards[0].values():
        return 1
    elif 3 in cards[1].values():
        return - 1
    
    #Two pair
    elif sum([val == 2 for val in cards[0].values()]) == 2 and sum([val == 2 for val in cards[1].values()]) == 2:
        count = 0
        while values[hand1[count]] == values[hand2[count]]:
            count += 1
        return 1 if values[hand1[count]] >= values[hand2[count]] else -1

    elif sum([val == 2 for val in cards[0].values()]) == 2:
        return 1
    elif sum([val == 2 for val in cards[1].values()]) == 2:
        return - 1
    
    #One pair
    elif 2 in cards[0].values() and 2 in cards[1].values():
        count = 0
        while values[hand1[count]] == values[hand2[count]]:
            count += 1
        return 1 if values[hand1[count]] >= values[hand2[count]] else -1

    elif 2 in cards[0].values():
        return 1
    elif 2 in cards[1].values():
        return - 1
    
    else:
        count = 0
        while values[hand1[count]] == values[hand2[count]]:
            count += 1
        return 1 if values[hand1[count]] >= values[hand2[count]] else -1


def part1(data: list[str]) -> int:
    hands = {}
    for l in data:
        hand, bid = l.split()
        bid = int(bid)
        
        hands[hand] = (0, bid)
    
    key_func = cmp_to_key(is_greater_than)
    sorted_hands_keys = sorted(hands, key=key_func)
    total = 0
    for i, hand_key in enumerate(sorted_hands_keys):
        bid = hands[hand_key][1]
        total += (i+1) * bid

    return total

def part2(data: list[str]) -> int:
    hands = {}
    for l in data:
        hand, bid = l.split()
        bid = int(bid)
        
        hands[hand] = (0, bid)
    
    key_func = cmp_to_key(lambda hand1, hand2: is_greater_than(hand1, hand2, jollys=True))
    sorted_hands_keys = sorted(hands, key=key_func)
    total = 0
    for i, hand_key in enumerate(sorted_hands_keys):
        bid = hands[hand_key][1]
        total += (i+1) * bid

    return total

if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read()
    print(part1(DEBUG.splitlines()))
    advent.print_answer(1, part1(data.splitlines()))
    print(part2(DEBUG.splitlines()))
    advent.print_answer(2, part2(data.splitlines()))