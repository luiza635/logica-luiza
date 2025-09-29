from random import randint

computador = randint(1, 20)

while True:
    user = int(input('Digite um número: '))
    if user < computador:
        print('O número é maior')    
    elif user > computador:
        print('O número é menor')
    else:
        print('Parabéns você acertou!')
        break