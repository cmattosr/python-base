"""
Exemplos de envio de e-mail

antes de rodar esse programa:
- iniciar o servidor smtp:
    python -m smtpd -c DebuggingServer -n localhost:8025
"""
import smtplib


SERVER = "localhost"
PORTA = 8025


FROM = "cmrocha@gmail.com"
TO = ["cmrocha+1@gmail.com", "cmrocha+3@gmail.com"]
SUBJECT = "Meu email via Python"
TEXT = """\
Este é o meu e-mail enviado pelo Python
<b>Olá, Mundo</b>    
"""

# SMTP
mensagem = f"""\
From: {FROM}
To: {", ".join(TO)}
Subject: {SUBJECT}

{TEXT}
"""

with smtplib.SMTP(host=SERVER, port=PORTA) as server:
    server.sendmail(FROM, TO, mensagem.encode("utf-8"))