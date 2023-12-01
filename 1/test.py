with open('1/test.txt', 'r') as f:
    s = f.read()

sum = 0
found_und1 = False
for i,char in enumerate(s):
    if char == '(':
        sum += 1
    elif char == ')':
        sum = sum - 1
    
    else:
        print('error')
    if sum == -1 and not found_und1:
        print(i+1)
        found_und1 = True
print(sum)