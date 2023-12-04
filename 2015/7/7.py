with open("2015/7/input.txt", 'r') as f:
    list = f.read().split('\n')

es = """
123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
"""

vars = {}
book = {}
def operate(a, b, to, op):
    if op == 'NOT':
        vars[to] = ~vars[b]
    elif op == 'AND':
        if a in vars:
            aa = vars[a]
        else:
            aa = int(a)
        if b in vars:
            bb = vars[b]
        else:
            bb = int(b)
        vars[to] = aa & bb
    elif op == 'OR':
        if a in vars:
            aa = vars[a]
        else:
            aa = int(a)
        if b in vars:
            bb = vars[b]
        else:
            bb = int(b)
        vars[to] = aa | bb
    elif op == 'LSHIFT':
        if a in vars:
            aa = vars[a]
        else:
            aa = int(a)
        vars[to] = aa * 2 * int(b)
    elif op == 'RSHIFT':
        if a in vars:
            aa = vars[a]
        else:
            aa = int(a)
        vars[to] = aa / (2 * int(b))

operators = ['AND', 'OR', 'LSHIFT', 'RSHIFT', 'NOT']


for r in list:
    lhs, rhs = [x.strip() for x in r.split('->')]
    book[rhs] = lhs

def find_ops(to):
    lhs = book[to]
    terms = lhs.split()
    for i, term in enumerate(terms):
        if term not in operators and not term[0].isdigit():
            terms[i] = find_ops(term)
    return terms


 
print(find_ops('a'))



#if op:
#                if operators[i] == 'NOT':
#                    b = lhs.split()[1]
#                    operate(None, b, rhs, 'NOT')
#                else:
#                    a, operator, b = [k.strip() for k in lhs.partition(operators[i])]
#                    operate(a, b, rhs, operator)