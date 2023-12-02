with open("2015/3/input.txt", 'r') as f:
    path = f.read()

houses = 0
x = 0
y = 0

spos = (x,y)
rpos = (x,y)

map = {'^':(0,1),'>':(1,0),'v':(0,-1),'<':(-1,0)}

sposhist = []
rposhist = []

for i,p in enumerate(path):
    if i%2 == 0:
        #santa
        operator =  map[p]
        x = spos[0] + operator[0]
        y = spos[1] + operator[1]
        spos = (x,y)
        sposhist.append(spos)

    else:
        #robo
        operator =  map[p]
        x = rpos[0] + operator[0]
        y = rpos[1] + operator[1]
        rpos = (x,y)
        rposhist.append(rpos)

sposhist.extend(rposhist)
houses = len(set(sposhist))
print(houses)