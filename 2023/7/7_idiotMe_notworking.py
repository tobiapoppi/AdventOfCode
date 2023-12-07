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

order = list('AKQJT98765432')
orderp2 = list('AKQT98765432J')
counter = itertools.count()

def is_greater_than_DUMB(hand1, hand2):
    # Your comparison logic here
    # Return a positive number if hand1 > hand2, negative if hand1 < hand2, and 0 if they are equal
    values = defaultdict(list)
    for key, value in zip(reversed(order), counter):
        values[key].append(value)
    
    cards_1 = {}
    cards_2 = {}

    for c1,c2 in zip(hand1, hand2):
        if c1 not in cards_1:
            cards_1[c1] = 0
        cards_1[c1] += 1
        if c2 not in cards_2:
            cards_2[c2] = 0
        cards_2[c2] += 1

    #for (card1, count1),(card2, count2) in zip(cards_1.items(), cards_2.items()):
    if 5 in cards_1.values() and 5 in cards_2.values():
        c1 = [card for card,val in cards_1.items() if val == 5][0]
        c2 = [card for card,val in cards_2.items() if val == 5][0]
        return 1 if values[c1] > values[c2] else -1
    elif 5 in cards_1.values():
        return 1
    elif 5 in cards_2.values():
        return -1
    
    elif 4 in cards_1.values() and 4 in cards_2.values():
        c1 = [card for card,val in cards_1.items() if val == 4][0]
        c2 = [card for card,val in cards_2.items() if val == 4][0]
        return 1 if values[c1] > values[c2] else -1
    elif 4 in cards_1.values():
        return 1
    elif 4 in cards_2.values():
        return -1

    elif 3 in cards_1.values() and 2 in cards_1.values() and 3 in cards_2.values() and 2 in cards_2.values():
        c1 = [card for card,val in cards_1.items() if val == 3][0]
        c2 = [card for card,val in cards_2.items() if val == 3][0]
        if c1 == c2:
            c1 = [card for card,val in cards_1.items() if val == 2][0]
            c2 = [card for card,val in cards_2.items() if val == 2][0]
        return 1 if values[c1] >= values[c2] else -1
    elif 3 in cards_1.values() and 2 in cards_1.values():
        return 1
    elif 3 in cards_2.values() and 2 in cards_2.values():
        return - 1
    
    elif 3 in cards_1.values() and 3 in cards_2.values() :
        c1 = [card for card,val in cards_1.items() if val == 3][0]
        c2 = [card for card,val in cards_2.items() if val == 3][0]

        if c1 == c2:
            c1 = [card for card,val in cards_1.items() if val == 1]
            c1 = max([val for c in c1 for val in values[c]])
            c2 = [card for card,val in cards_2.items() if val == 1]
            c2 = max([val for c in c2 for val in values[c]])
        return 1 if values[c1] > values[c2] else -1
    elif 3 in cards_1.values():
        return 1
    elif 3 in cards_2.values():
        return - 1
    
    #Two pair
    elif sum([val == 2 for val in cards_1.values()]) == 2 and sum([val == 2 for val in cards_2.values()]) == 2:
        c1 = [card for card,val in cards_1.items() if val == 2]
        c2 = [card for card,val in cards_2.items() if val == 2]
        c1 = max([val for c in c1 for val in values[c]])
        c2 = max([val for c in c2 for val in values[c]])

        if c1 == c2:
            c1 = [card for card,val in cards_1.items() if val == 1]
            c1 = max([val for c in c1 for val in values[c]])
            c2 = [card for card,val in cards_2.items() if val == 1]
            c2 = max([val for c in c2 for val in values[c]])

        return 1 if values[c1] > values[c2] else -1

    elif sum([val == 2 for val in cards_1.values()]) == 2:
        return 1
    elif sum([val == 2 for val in cards_2.values()]) == 2:
        return - 1
    
    #One pair
    elif 2 in cards_1.values() and 2 in cards_2.values():
        c1 = [card for card,val in cards_1.items() if val == 2][0]
        c2 = [card for card,val in cards_2.items() if val == 2][0]


        if c1 == c2:
            c1 = [card for card,val in cards_1.items() if val == 1]
            c1 = max([val for c in c1 for val in values[c]])
            c2 = [card for card,val in cards_2.items() if val == 1]
            c2 = max([val for c in c2 for val in values[c]])

            return 1 if c1 > c2 else -1

        return 1 if values[c1] > values[c2] else -1

    elif 2 in cards_1.values():
        return 1
    elif 2 in cards_2.values():
        return - 1
    
    else:
        c1 = max([val for c in cards_1.keys() for val in values[c]])
        c2 = max([val for c in cards_2.keys() for val in values[c]])
        return 1 if c1 > c2 else -1
    

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
    pass

if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read()
    print(part1(DEBUG.splitlines()))
    advent.print_answer(1, part1(data.splitlines()))
    #print(part2(DEBUG.splitlines()))
    #advent.print_answer(2, part2(data.splitlines()))