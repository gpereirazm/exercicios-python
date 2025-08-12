def valores_unicos(lista):
    lista_unica = []
    for numero in lista:
        if numero not in lista_unica:
            lista_unica.append(numero)
    return lista_unica

numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999,
           5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

print("Valores únicos:", valores_unicos(numeros))
