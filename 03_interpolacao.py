import sys
import os

arguments = sys.argv[1:]

if not arguments:
    print("Informe o nome do arquivo de emails")
    sys.exit(1)
    
filename = arguments[0]
template_name = arguments[1]
path = os.curdir
filepath = os.path.join(path, filename) #emails.txt
templatepath = os.path.join(path, template_name) #email_template.txt

for linha in open(filepath):
    nome, email = linha.split(",")
    print(f"Enviando email para: {email}")
    print()
    print(
        open(templatepath).read()
        % {
            "nome": nome, 
            "produto": "caneta", 
            "texto": "escrever muito bem", 
            "link": "www.canetaslegais.com.br", 
            "quantidade": 2, 
            "preco": 50.5,
            }
        )
    print("-" * 50)
