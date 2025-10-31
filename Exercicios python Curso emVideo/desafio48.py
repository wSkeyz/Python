soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
    else:
        continue
print("A soma de todos os valores multiplos de 3 entre 1 e 500 é {}".format(soma))