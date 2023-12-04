with open('4/input.txt', 'r') as f:
    cards = f.read().split('\n')

def calculate_points(cards):
    total_points = 0

    #part1
    for card in cards:
        winning_numbers, your_numbers = card.split(' | ')
        winning_numbers = winning_numbers.split(':')[1]
        winning_numbers = set(map(int, winning_numbers.split()))
        your_numbers = set(map(int, your_numbers.split()))

        matches = winning_numbers.intersection(your_numbers)
        if matches:
            total_points += 2 ** (len(matches) - 1)
        else:
            pass
    
    #part2
    n = len(cards)
    card_instances = [1] * n

    for i in range(n):
        winning_numbers, your_numbers = cards[i].split(' | ')
        winning_numbers = winning_numbers.split(':')[1]
        winning_numbers = set(map(int, winning_numbers.split()))
        your_numbers = set(map(int, your_numbers.split()))

        nmatches = len(winning_numbers.intersection(your_numbers))
        for j in range(i+1, min(i+1+nmatches, n)):
            card_instances[j] += card_instances[i]

    return total_points, sum(card_instances)

print(calculate_points(cards))

