with open("2015/2/input.txt", 'r') as f:
    list = f.read().split('\n')

tot = 0
mintotal = 0
ribbon = 0
for solid in list:
    lwh = solid.split('x')
    l, w, h = [int(i) for i in lwh]
    tot += (2*l*w) + (2*w*h) + (2*h*l)
    mintotal += min(l*w, w*h, h*l)
    ribbon += l*w*h
    lwh = [l,w,h]
    lwh.sort()
    ribbon += lwh[0]*2 + lwh[1]*2


print(tot+mintotal)
print(ribbon)