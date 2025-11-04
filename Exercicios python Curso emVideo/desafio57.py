nome = input("Qual seu nome? ")
sexo = input("Qual seu sexo? [M/F] ").upper()
while sexo != "M" and sexo != "F":
    sexo = input("Sexo inválido, digite novamente seu sexo: [M/F] ").upper()
print(f"Seu nome é {nome} e seu sexo é {sexo}")