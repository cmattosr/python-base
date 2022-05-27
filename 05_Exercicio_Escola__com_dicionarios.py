#fazer depois

#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.
Imprimir a lista de crianças agrupadas por sala
que frequentas cada uma das atividades.
"""
__version__ = "0.1.3"

########################################################
#      ATENçÃO: MODIFIQUE ESSE CÓDIGO!                 #
#   Tente utilizar dicionários onde achar conveniente  #
########################################################

# Dados
dados = {
    "sala1": ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
    "sala2": ["Joao", "Antonio", "Carlos", "Maria", "Isolda"],
}

atividades = {
    "Inglês": ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
    "Música": ["Erik", "Carlos", "Maria"],
    "Dança": ["Gustavo", "Sofia", "Joana", "Antonio"],
}

for nome_atividade, aluno in atividades.items():
    
    print(f"Alunos da atividade {nome_atividade}\n")
    print("-" * 40)

    atividade_sala1 = set(dados["sala1"]) & set(aluno)
    atividade_sala2 = set(dados["sala2"]) & set(aluno)

    print("sala1", atividade_sala1)
    print("Sala2", atividade_sala2)

    print()
    print("#" * 40)
    print()