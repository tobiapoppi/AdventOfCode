import hashlib

input = 'ckczppom'
n = 0

res = hashlib.md5(f'{input}{n}'.encode()).hexdigest()
while res[:6] != '000000':
    n += 1
    res = hashlib.md5(f'{input}{n}'.encode()).hexdigest()
print(n)
print(res)
