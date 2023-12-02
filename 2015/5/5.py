with open("2015/5/input.txt", 'r') as f:
    list = f.read().split('\n')
voc = 'aeiou'
banned = ['ab', 'cd', 'pq', 'xy']

numnice = 0
for s in list:
    ok = True
    for b in banned:
        if b in s:
            ok = False
    if ok:
        vocals = 0
        for c in s:
            if c in voc:
                vocals += 1
        if vocals < 3:
            ok = False
    if ok:
        for i, c in enumerate(s[1:]):
            prec = s[i]
            if c == prec:
                numnice += 1
                break
print(numnice)

numnice = 0
for s in list:
    ok = False
    for i in range(1,len(s)-1):
        prec = s[i-1]
        succ = s[i+1]
        if succ == prec:
            ok = True
    if ok:
        for i in range(len(s)):
            sub = s[i:i+2]
            if sub in s[i+2:]:
                ok = True
                numnice += 1
                break

print(numnice)
