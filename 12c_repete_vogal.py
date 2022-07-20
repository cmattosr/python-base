palavras = []
while True:
    palavra = input("Digite uma palavra (ou enter para sair): ").strip()
    if not palavra: #condição de parada
        break
    palavra_final = ""
    for letra in palavra:
        """
        if letra.lower() in "aeiouãõáéêô":
            palavra_final += letra * 2
        else:
            palavra_final += letra 
        """
        #solução usando if ternário
        palavra_final += letra * 2 if letra.lower() in "aeiouãõáéêô" else letra
    palavras.append(palavra_final)
    
# for palavra in palavras:
#     print(palavra)
print(*palavras, sep="\n")