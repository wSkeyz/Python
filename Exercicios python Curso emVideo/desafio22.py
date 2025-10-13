nome = input("digite seu nome completo:")
nome2 = nome.split()[0]
print(nome.upper())
print(nome.lower())
print(len(nome.replace(" ", "")))
print("seu primeiro nome e {} e tem {} letras".format (nome2, len(nome2)))