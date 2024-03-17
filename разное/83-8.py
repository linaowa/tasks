from .model import calc

def calc(expr):
    pos = lastOp(expr)
    if pos < 0:
        return int(expr)
    else:
        n1 = calc(expr[:pos])       # левая часть
        n2 = calc(expr[pos + 1:])   # правая часть
        return doOperation(expr[pos], n1, n2)

def doOperation(op, n1, n2):
    if op == '+': return n1 + n2
    elif op == '-': return n1 - n2
    elif op == '*': return n1 * n2
    else:           return n1 // n2

def priority(op):
    if op in '+-': return 1
    if op in '*/': return 2
    return 100 # условное значение 

def lastOp(expr):
    minPrt = 50
    pos = -1
    for i in range(len(expr)):
        prt = priority(expr[i])
        if prt <= minPrt:
            minPrt = prt
            pos = i
    return pos