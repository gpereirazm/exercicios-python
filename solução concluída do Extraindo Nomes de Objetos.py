class Pessoa:
    def __init__(self, nome):
        self.nome = nome

def extrair_nomes(lista_objetos):
    nomes = []
    for obj in lista_objetos:
        nomes.append(obj.nome)
    return nomes

pessoas = [Pessoa("Ana"), Pessoa("Bruno"), Pessoa("Carlos")]

nomes = extrair_nomes(pessoas)
print(nomes)  

