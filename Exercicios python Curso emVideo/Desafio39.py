Datanascimento = int(input("Qual o ano do seu Nascimento?:"))
idade = 2025 - Datanascimento 

if idade == 18:
    print("Voce tem que se alistar esse ano.")

elif idade > 18:
    print("Ja se passaram {} Anos do seu alistamento militar.".format((2025 - Datanascimento) - 18))

elif idade < 18:
    print("Ainda Faltam {} Anos para o alistamento militar.".format(idade))