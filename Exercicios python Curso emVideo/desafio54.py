maior = 0
for i in range(0, 7):
    nascimento = int(input("Ano de nascimento:"))
    if 2025 - nascimento >= 21:
        maior = maior + 1
    else:
        continue
print("Ao todo tivemos {} pessoas maiores de idade".format(maior))