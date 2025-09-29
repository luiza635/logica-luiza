par = impar = 0

for i in range(1, 11):
    num = int(input('Digite um número: '))
    if num  %  2 == 0:
        par += 1
    else:
        impar += 1
        
print(f'Você digitou {par} números pares')
print(f'Você digitou {impar} números ímpares')