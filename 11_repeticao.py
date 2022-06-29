original = [1,2,3]  

# For loops / Laço FOR
dobrada = []
for n in original:
    dobrada.append(n*2)  
print(dobrada)


# List Comprehension
dobrada = [n*2 for n in original]
print(dobrada)

# Dict Comprehension
dados = {line.split(",")[0] : line.split(",")[1].strip() for line in open("emails.txt")}
print(dados)
