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

nsolved = 0
vars = {}

#part 1
#book = {}

#part 2
book = {'b': 46065}
def operate(a, b, op):
    if op == 'NOT':
        return int(~a)
    elif op == 'AND':
        return int(a & b)
    elif op == 'OR':
        return int(a | b)
    elif op == 'LSHIFT':
        return int(a << b)
    elif op == 'RSHIFT':
        return int(a >> b)

def replace_all_solved_vals(book, nsolved, already):
    solved_vars = []
    for var, val in book.items():
        if not len(val) - 1 and type(val[0]) == int:
            solved_vars.append(var)
            if var not in already:
                already.append(var)
                nsolved += 1

    for v in solved_vars:
        for var in book.keys():
            book[var] = [book[v][0] if i == v else i for i in book[var]]
    #print(f'{len(solved_vars)}/{len(book)} elements solved!')
    return nsolved

def solve_solvable(book, nsolved, already):
    count = 0
    for var, val in book.items():
        if not len(val) - 1:
            continue
        if all([type(v) == int or v in operators for v in val]):
            #solve
            if not len(val) - 2:
                book[var] = [operate(val[1], None, val[0])]
            elif not len(val) - 3:
                book[var] = [operate(val[0], val[2], val[1])]
            else:
                print('error')
                return 0
            already.append(var)
            count += 1
            nsolved += 1
    #print(f'Solved {nsolved}/{len(book)} variables')
    return nsolved

already_solved = []
operators = ['AND', 'OR', 'LSHIFT', 'RSHIFT', 'NOT']

for r in list:
    lhs, rhs = [x.strip() for x in r.split('->')]
    lhs = [int(t) if t[0].isdigit() else t for t in lhs.split()] 
    book[rhs] = lhs

while(type(book['a'][0]) != int):
    nsolved = replace_all_solved_vals(book, nsolved, already_solved)
    nsolved = solve_solvable(book, nsolved, already_solved)
    if nsolved == 0:
        break
 
print(book['a'])



#if op:
#                if operators[i] == 'NOT':
#                    b = lhs.split()[1]
#                    operate(None, b, rhs, 'NOT')
#                else:
#                    a, operator, b = [k.strip() for k in lhs.partition(operators[i])]
#                    operate(a, b, rhs, operator)