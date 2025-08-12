def media_aritmetica(lista):
    if len(lista) == 0:
        return 0 
    soma = 0
    for numero in lista:
        soma += numero
    media = soma / len(lista) 
    return media

numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999,
           5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

print("A média dos números é:", media_aritmetica(numeros))
