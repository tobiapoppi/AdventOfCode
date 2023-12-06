with open("2015/8/input.txt", 'r') as f:
    ls = f.read().split('\n')

es = r"""""
"abc"
"aaa\"aaa"
"\x27"
"""

#ls = str(es).split('\n')

ncode = 0
nchars = 0

#part 1
ignore_next = 0
for s in ls:
    new_nchars = 0
    ncode += len(s)
    new_s = s[1:-1]
    for i,c in enumerate(new_s):
        if ignore_next > 0:
            ignore_next += -1
            continue
        if i == len(new_s)-1:
            new_nchars += 1
            continue
        if c == '\\' and new_s[i+1] == '\\':
            ignore_next = 1
            new_nchars += 1
            continue
        if c == '\\' and new_s[i+1] == 'x':
            ignore_next = 3
            new_nchars += 1
            continue
        elif c == '\\' and new_s[i+1] != '\\':
            continue
        new_nchars += 1
    nchars += new_nchars

print(ncode)
print(nchars)
print(ncode-nchars)

#part 2
ncode = 0
nchars = 0
for s in ls:
    part_ncode = len(s)
    new_nchars = 4 + part_ncode
    new_s = s[1:-1]
    for i,c in enumerate(new_s):
        if i == len(new_s)-1:
            continue
        #eval(c)
        if c == '\\' and new_s[i+1] == '\\':
            new_nchars += 1
        elif c == '\\' and new_s[i+1] == 'x':
            new_nchars += 1
        elif c == '\\' and new_s[i+1] != '\\':
            new_nchars += 2
    nchars += new_nchars
    ncode += part_ncode

print('Part 2')
print(ncode)
print(nchars)
print(nchars-ncode)