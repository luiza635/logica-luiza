notas = [10, 7, 8, 9.5, 6]

# def media(lista : list) -> float:
#     soma = cont = 0
#     for nota in lista:
#         soma += nota
#         cont += 1
#     return soma / cont

def media(lista):
    return sum(lista) / len(lista)

print(media(notas))
    