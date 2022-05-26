"""Hello World Multi Linguas.

Dependendo da língua configurada no ambiente, o programa exibe a mensagem correspondente.

Como usar:
tenha a variável LANG devidamente configurada no ambiente, ex:
    export LANG=pt_BR.UTF-8
    (dependendo do Sistma Operacional a configuração de variável de ambiente muda)
    
Ou informe através do CLI argument "--lang"

Ou o usuário terá que digitar
    
Execução:

    python3 hello.py
"""

__version__ = "0.1.3"
__author__ = "Cesar Mattos Rocha"
__license__ = "Unlicense"

import os
import sys

arguments = {"lang": None, "count" : 1}

for arg in sys.argv[1:]:
    # TODO: Tratar ValueError (argumento inválido, sem o '=')
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Argumento inválido: '{key}'")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    current_language = os.getenv("LANG")
    # TODO: Usar repetição
    if current_language is None:
        current_language = input("Choose a language: ")
    
current_language = current_language[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "¡Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!"
}

# sets implementam Hash Table = ordem de complexidade O(1) - constante
# dicionários também implementam Hash Table

print((msg[current_language] + "\n" )* int(arguments["count"]))
