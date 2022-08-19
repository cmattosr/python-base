# Digamos que tenhamos uma coleção de utilidades

def transforma_em_maiusculo(texto):
    return texto.upper()


def transforma_em_minusculo(texto):
    return texto.lower()


def divide_por_2(numero):
    return numero // 2


# e nossa função principal

def faz_algo(valor, funcao):
    print(f"Aplicando a {funcao} em {valor}")
    return funcao(valor)

print(faz_algo("bruno", transforma_em_maiusculo))
# BRUNO

print(faz_algo("BRUNO", transforma_em_minusculo))
# bruno

print(faz_algo(10, divide_por_2))
# 5

print(faz_algo(10, lambda x: x * 2))
# 20
print(faz_algo(10, lambda x: x // 2))
# 5
print(faz_algo("python é bom", lambda x: x.title()))
# Python É Bom


nomes = ["Bruno", "João", "Maria", "Carlos", "Erik"]
print("Por tamanho: ", sorted(nomes, key=len))
# ['João', 'Erik', 'Bruno', 'Maria', 'Carlos']

print("Por letras 'a': ", sorted(nomes, key=lambda name: name.count("a")))

print("Que começam bom 'B': ",list(filter(lambda x: x.startswith("B"), nomes)))
# ['Bruno']