Ano_nascimento = int(input("Digite o ano de nascimento do atleta:"))
Idade = 2025 - Ano_nascimento
if Idade <= 9:
    print("MIRIM")
elif Idade <= 14:
    print("INFANTIL")
elif Idade <= 19:
    print("JUNIOR")
elif Idade <= 20:
    print("SÊNIOR")
else:
    print("MASTER")