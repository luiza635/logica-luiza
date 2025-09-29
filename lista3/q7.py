# 5! = 5 x 4 x 3 x 2 x 1 = 120

def fatorial(num):
    resultado = 1
    for i in range(1, num+1):
        resultado *= i
    return resultado

print(fatorial(5))