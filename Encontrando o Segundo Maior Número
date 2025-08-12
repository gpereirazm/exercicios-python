def segundo_maior(lista):
    
    if len(set(lista)) < 2:
        return None 

    maior = max(lista)  # acha o maior número
    
    lista_sem_maior = [num for num in lista if num != maior]

    return max(lista_sem_maior)

numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999,
           5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

print("O segundo maior número é:", segundo_maior(numeros))
