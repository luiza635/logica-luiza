def contador(palavra):
    cont = 0
    for letra in palavra:
        if letra in 'aeiou':
            cont+=1
    return cont