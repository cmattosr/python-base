email_tmpl = """
Olá, %(nome)s,

Tem interesse em comprar %(produto)s?
Este produto é ótimo para resolver %(texto)s
Clique agora em %(link)s
Apenas %(quantidade)d disponíveis!
Preço promocional: %(preco).2f
"""

clientes = ["Maria", "João", "Bruno"]

for cliente in clientes:
    print(email_tmpl % {"nome": cliente, "produto": "caneta", "texto": "Escrever muito bem", "link": "www.canetaslegais.com.br", "quantidade": 1, "preco": 58.23})
