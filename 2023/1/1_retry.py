def getNumber(s, last=False):
    if last:
        s = s[::-1]
    for i in range(len(s)):
        if s[i].isdigit():
            return s[i]
        for num in d:
            if s[i:].startswith(num if not last else num[::-1]):
                return d[num]


with open('1/input.txt', 'r') as f:
    list = f.read().split('\n')

d = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}

sum = 0
for s in list:
    a = getNumber(s)
    b = getNumber(s, last=True)
    sum += int(a+b)

print(sum)