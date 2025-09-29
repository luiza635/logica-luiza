def inverter(palavra):
    tam = len(palavra)
    reverso = ''
    for letra in palavra:
        reverso += palavra[tam-1]
        tam -= 1
    return reverso
    
print(inverter('Luiza'))