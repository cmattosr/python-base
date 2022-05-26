"""Hello World Multi Linguas.

Dependendo da língua configurada no ambiente, o programa exibe a mensagem correspondente.

Como usar:
tenha a variável LANG devidamente configurada no ambiente, ex:
    export LANG=pt_BR.UTF-8
dependendo do Sistma Operacional a configuração de variável de ambiente muda
    
Execução:

    python3 hello.py
"""

__version__ = "0.1.0"
__author__ = "Cesar Mattos Rocha"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, World!"

# Ordem de complexidade O(n) - linear
if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "¡Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour, Monde!"

print(msg)
