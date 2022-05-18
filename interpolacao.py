email_tmpl = """
Olá, %(nome)s,

Tem interesse em comprar %(produto)s?
Este produto é ótimo para %(texto)s
Clique agora em %(link)s
Apenas %(quantidade)d disponíveis!
Preço promocional: %(preco).2f
"""

clientes = ["Maria", "João", "Bruno"]
preco = [344.1, 85.45, 984.77]

for i, cliente in enumerate(clientes):
    print(email_tmpl % {"nome": cliente, "produto": "caneta", "texto": "escrever muito bem", "link": "www.canetaslegais.com.br", "quantidade": 1, "preco": preco[i]})
