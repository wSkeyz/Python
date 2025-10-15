nome = str(input("Qual e seu nome?")).strip().capitalize()
if nome == "Alex":
    print("Bom dia nome bonito")
elif nome == "Fran":
    print("Nome da minha namorada")
elif nome in "Ana maria braga":
    print("Voce e do progama de tv?")
else:
    print("Seu nome e {}".format(nome))     