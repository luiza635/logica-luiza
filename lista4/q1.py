pessoas = [] # lista
cont = 0

for i in range(1, 6):
    nome = input(f"Digite o {i}° nome: ")
    pessoas.append(nome)
    if nome[0] in "AaÁá":
        cont += 1

for pessoa in pessoas:
    print(pessoa)
print(f"Número de pessoas que começam com a letra A: {cont}")
