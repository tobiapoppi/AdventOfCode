with open("2015/6/input.txt", 'r') as f:
    list = f.read().split('\n')


def action(a, b, act, grid):
    for r in range(b[0] - a[0] + 1):
        for c in range(b[1] - a[1] + 1):
            if act == 'turn on':
                grid[a[0]+r][a[1]+c] = 1
            elif act == 'turn off':
                grid[a[0]+r][a[1]+c] = 0
            elif act == 'toggle':
                grid[a[0]+r][a[1]+c] = 0 if grid[a[0]+r][a[1]+c] == 1 else 1

def newaction(a, b, act, grid):
    for r in range(b[0] - a[0] + 1):
        for c in range(b[1] - a[1] + 1):
            if act == 'turn on':
                grid[a[0]+r][a[1]+c] += 1
            elif act == 'turn off':
                grid[a[0]+r][a[1]+c] = max(0, grid[a[0]+r][a[1]+c] - 1)
            elif act == 'toggle':
                grid[a[0]+r][a[1]+c] += 2

grid = [[0 for _ in range(1000)] for _ in range(1000)]


for r in list:
    act_a, b = r.split('through')
    b = tuple(int(x) for x in b.strip().split(','))
    act,a = act_a.strip().rsplit(' ', maxsplit=1)
    a = tuple(int(x) for x in a.strip().split(','))
    newaction(a, b, act, grid)

print(sum([sum(i) for i in grid]))

