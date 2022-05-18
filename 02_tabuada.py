"""Imprime a tabuada do 1 ao 10"""
__version__ = "1.1"
__author__ = "Cesar Mattos Rocha"

template_base = """
---Tabuada do 2---
        
   {bloco_texto:^18}

##################
"""

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = list(range(1, 11))

# Iterable (percorrível)
for n1 in numeros:
    print("{:-^18}".format(f"Tabuada do {n1}"))
    print()
    for n2 in numeros:
        resultado = n1 * n2
        print("{:^18}".format(f"{n1} x {n2} = {resultado}"))
        
    print("#" * 18)
