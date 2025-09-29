num = int(input('Digite um número: '))
cont = 0
for n in range(1, num+1):
    if n % 2 == 0:
        cont += n
print(cont)