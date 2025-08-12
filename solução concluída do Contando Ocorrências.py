def contar_ocorrencias(lista, valor):
    contador = 0
    for elemento in lista:
        if elemento == valor:
            contador += 1  
    return contador

numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999,
           5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

valor_procurado = 13
total = contar_ocorrencias(numeros, valor_procurado)
print(f"O valor {valor_procurado} aparece {total} vezes na lista.")
