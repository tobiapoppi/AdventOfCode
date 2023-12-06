with open('2023/6/input.txt', 'r') as f:
    lines = f.read().split('\n')
import math
import tqdm

inp = """
Time:        42     68     69     85
Distance:   284   1005   1122   1341"""

times = [42, 68, 69, 85]
distances = [284, 1005, 1122, 1341]

#times = [7,  15,   30]
#distances = [9, 40,  200]

times = 71530
distances = 940200


times = 42686985
distances = 284100511221341


speed = 0
diff_speed = 1

wayys_to_win = []

#for k, t in enumerate(times):
#    ways = 0
#    for i in range(t+1):
#        if ((t-i) * i) > distances[k]:
#            ways += 1
#    wayys_to_win.append(ways)
ways = 0
for i in tqdm.tqdm(range(times+1)):
    if ((times-i) * i) > distances:
        ways += 1

print(ways)

print(wayys_to_win)
print(math.prod(wayys_to_win))