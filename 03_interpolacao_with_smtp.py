"""

antes de rodar esse programa:
- iniciar o servidor smtp:
    python -m smtpd -c DebuggingServer -n localhost:8025
    
para executar:  
py .\03_interpolacao_with_smtp.py emails.txt .\email_template.txt
"""
import sys
import os
import smtplib
from email.mime.text import MIMEText


arguments = sys.argv[1:]

if not arguments:
    print("Informe o nome do arquivo de emails")
    sys.exit(1)
    
filename = arguments[0]
template_name = arguments[1]
path = os.curdir
filepath = os.path.join(path, filename) #emails.txt
templatepath = os.path.join(path, template_name) #email_template.txt

with smtplib.SMTP(host="localhost", port=8025) as server:

    for linha in open(filepath):
        nome, email = linha.split(",")
        texto = (
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
        
        from_ = "cmrocha@gmail.com"
        to = ", ".join([email])
        message = MIMEText(texto)
        message["Subject"] = "Compre mais"
        message["From"] = from_
        message["To"] = to
        
        server.sendmail(from_, to, message.as_string())
