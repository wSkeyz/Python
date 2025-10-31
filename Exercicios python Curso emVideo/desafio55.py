peso_maior = 0
peso_menor = 0
for i in range(1, 6):
    peso = float(input("Digite peso da {}ª pessoa: ".format(i)))
    if i == 1:
        peso_maior = peso_menor = peso
    else:
        if peso > peso_maior:
            peso_maior = peso
        if peso < peso_menor:
            peso_menor = peso
print("O maior peso lido foi {}kg".format(peso_maior))
print("O menor peso lido foi {}kg".format(peso_menor))