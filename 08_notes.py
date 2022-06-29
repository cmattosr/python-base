""" Bloco de Notas
$ 08_notes.py new "Minha Nota"
tag: tech
text:
Anotacao geral sobre carreira de tecnologia
$ 08_notes.py read --tag=tech
"""

__version__ = "0.1.0"

import os
import sys

path = os.curdir
filepath = os.path.join(path, "08_notes.txt")

cmds = ("read", "new")
arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage")
    print(f"You must specify a subcommand: {cmds}")
    sys.exit(1)

if arguments[0] not in cmds:
    print("Invalid command {arguments[0]}")
    sys.exit(1)
    
while True:

    if arguments[0] == "read":
        try:
            _, tag = arguments[1].split("=")
        except IndexError:
            tag = input("Qual a tag? ")
        for linha in open(filepath):
            nota_arquivo, tag_arquivo, texto_arquivo = linha.split("\t")
            if tag.lower() == tag_arquivo.lower():
                print(nota_arquivo)
                print(texto_arquivo)
                #sys.exit(1)
            

    if arguments[0] == "new":
        notas = arguments[1] # TODO: Tratar exception
        text = [
            f"{notas}",
            input("tag: ").strip(),
            input("text:\n").strip()
        ]
        with open(filepath, "a") as file_:
            file_.write("\t".join(text) + "\n")
            
    continuar = input(f"Quer continuar {arguments[0]}? (N/y)").strip().lower()
    if continuar != "y":
        break