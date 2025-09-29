def calculadora(a, b, op):
    if op == '+' :
        return a + b
    elif op == '-' :
        return a - b
    elif op == '*' :
        return a * b
    elif op == '/' :
        return a / b

print(calculadora(10, 3, '+'))