from .model import calc

def calc(expr):
    try:
        pos = lastOp(expr)
        if pos < 0:
            return int(expr)
        else:
            n1 = calc(expr[:pos])       # левая часть
            n2 = calc(expr[pos + 1:])   # правая часть
            return doOperation(expr[pos], n1, n2)
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
        return None  # Можно вернуть какое-то значение по умолчанию или None

def doOperation(op, n1, n2):
    try:
        if op == '+':
            return n1 + n2
        elif op == '-':
            return n1 - n2
        elif op == '*':
            return n1 * n2
        elif op == '/':
            if n2 == 0:
                raise ZeroDivisionError("Division by zero")
            return n1 / n2
        else:
            raise ValueError("Invalid operator")
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
        return None  # Можно вернуть какое-то значение по умолчанию или None

def priority(op):
    if op in '+-':
        return 1
    elif op in '*/':
        return 2
    else:
        return 100  # условное значение 

def lastOp(expr):
    try:
        minPrt = 50
        pos = -1
        for i in range(len(expr)):
            prt = priority(expr[i])
            if prt <= minPrt:
                minPrt = prt
                pos = i
        if pos < 0:
            raise ValueError("No operator found")
        return pos
    except ValueError as e:
        print(f"Error: {e}")
        return None  # Можно вернуть какое-то значение по умолчанию или None
