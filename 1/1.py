def find_first_digit(s):
    word = ''
    for char in s:
        word += char
        for i in range(len(word)):
            substring = word[i:]
            if substring in map:
                return map[substring]
        if char.isdigit():
            return char
    return ''

def find_last_digit(s):
    word = ''
    for i,char in enumerate(reversed(s)):
        word = char + word
        for i in range(1, len(word) + 1):
            substring = word[:i]
            if substring in map:
                return map[substring]
        if char.isdigit():
            return char
    return ''



with open('1\input.txt', 'r') as f:
    list = f.read()

list = list.split('\n')


map = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}


total_sum = 0
for line in list:
    first_digit = find_first_digit(line)
    last_digit = find_last_digit(line)

    if first_digit and last_digit:
        total_sum += int(first_digit + last_digit)

print(total_sum)