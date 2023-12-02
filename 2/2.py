
with open('2\input.txt', 'r') as f:
    list = f.read()

list = list.split('\n')
games = {}
for l in list:
    content = l.split(':')[1]
    draws = content.split(';')
    newnewl = []
    for d in draws:
        cubes = d.split(',')
        newl = []
        for c in cubes:
            c = c.strip()
            c = c.replace(' ','_')
            newl.append(c)
        newnewl.append(newl)
    games[int(l.split(':')[0].split(' ')[1])] = newnewl

possibles = 0
sop = 0

for k, v in games.items():
    ok = True
    dic_max = {'red':0, 'green':0, 'blue':0}
    for d in v:
        for c in d:
            for color, max in {'red':12, 'green':13, 'blue':14}.items():
                if color in c:
                    if int(c.split('_')[0]) > max:
                        ok = False
                    if int(c.split('_')[0]) > dic_max[color]:
                        dic_max[color] = int(c.split('_')[0])

    if ok:
        possibles += int(k)
    
    power = 1
    for i in dic_max.values():
        power = power * i
    sop += power

print(possibles)
print(sop)