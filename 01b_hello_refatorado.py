"""Hello World Multi Linguas.

Dependendo da língua configurada no ambiente, o programa exibe a mensagem correspondente.

Como usar:
tenha a variável LANG devidamente configurada no ambiente, ex:
    export LANG=pt_BR.UTF-8
dependendo do Sistma Operacional a configuração de variável de ambiente muda
    
Execução:

    python3 hello.py
"""

__version__ = "0.1.2"
__author__ = "Cesar Mattos Rocha"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "¡Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!"
}

# sets implementam Hash Table = ordem de complexidade O(1) - constante
# dicionários também implementam Hash Table

print(msg[current_language])
