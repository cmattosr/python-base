from lib2to3.pgen2.token import RARROW
import sys
import logging

ocupados = {}
try:
    for line in open("12d_reservas.txt"):
        nome, num_quarto, dias = line.strip().split(",")
        ocupados[int(num_quarto)] = {
            "nome": nome,
            "dias": dias       
        }       
except FileNotFoundError:
    logging.error("Arquivo não existe")
    sys.exit(1)

quartos = {}
try:
    for line in open("12d_quartos.txt"):
        codigo, nome, preco = line.strip().split(",")
        quartos[codigo] = {
            "nome": nome,
            "preco": float(preco),    # TODO: Decimal
            "disponivel": False if int(codigo) in ocupados else True    
        }       
except FileNotFoundError:
    logging.error("Arquivo não existe")
    sys.exit(1)
     
print("Reserva Hotel Pythonico")
print("-" *40)

if len(ocupados) == len(quartos):
    print("Hotel Lotado!")
    sys.exit(1)
    
cliente = input("Nome do Cliente: ").strip()
print()
print("Lista de Quartos")
    
for codigo, dados in quartos.items():
    nome_quarto = dados["nome"]
    preco = dados["preco"]
    disponivel = "⛔" if not dados["disponivel"] else "👍"
    # outra maneira de fazer é a da linha abaixo
    # disponivel = dados["disponivel"] and "👍" or "⛔"
    print(f"{codigo} - {nome_quarto} - R$ {preco:.2f} - {disponivel}") 
    # TODO: Substituir casa decimal por virgula
    
print("-" *40)
    

try:
    num_quarto = input("Número do quarto: ")
    if not quartos[num_quarto]["disponivel"]:
        print(f"O quarto {num_quarto} está ocupado")
        sys.exit(1)
except ValueError:
    logging.error("Numero inválido, digite apenas número")
    sys.exit(1)
except KeyError:
    print(f"O quarto {num_quarto} não existe!")
    sys.exit(1)
    
try:
    dias = int(input("Quantos dias: ").strip())
except ValueError:
    logging.error("Numero inválido, digite apenas número")
    sys.exit(1)

nome_quarto = quartos[num_quarto]["nome"]  
preco_quarto = quartos[num_quarto]["preco"]  
disponivel = quartos[num_quarto]["disponivel"]  
total = preco_quarto * dias

with open("12d_reservas.txt", "a") as file_:
    file_.write(f"{cliente}, {num_quarto}, {dias}\n")


print(f"{cliente} você escolheu o quarto {nome_quarto} e custará R$ {total:.2f}")