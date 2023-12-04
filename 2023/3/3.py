with open('3/input.txt', 'r') as f:
    lines = f.read().split('\n')

total_sum = 0
gears = {}
for i, line in enumerate(lines):
    j = 0
    while j < len(line):
        if line[j].isdigit():
            # Extract the whole number
            num = ''
            while j < len(line) and line[j].isdigit():
                num += line[j]
                j += 1

            # Check adjacent cells for symbols (any character that's not a digit or period)
            part_number = False
            for di in range(-1, 2):
                for dj in range(-1, len(num)+1):
                    ni, nj = i + di, j - len(num) + dj
                    if 0 <= ni < len(lines) and 0 <= nj < len(line):
                        if not lines[ni][nj].isdigit() and lines[ni][nj] != '.':
                            part_number = True
                            if lines[ni][nj] == '*':
                                if f'({ni},{nj})' not in gears:
                                    gears[f'({ni},{nj})'] = []
                                gears[f'({ni},{nj})'].append(num)

            if part_number:
                total_sum += int(num)
        else:
            j += 1

sumratios = 0
for l in gears.values():
    if len(l) == 2:
        sumratios += (int(l[0])*int(l[1]))

print(total_sum)
print(sumratios)
