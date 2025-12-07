matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para [{i}, {j}]:"))
        linha.append(valor)
    matriz.append(linha)
print("-=" * 20)
for i in range(3):
    for j in range(3):
        print(f"[{matriz[i][j]:^4}]", end="")
    print()
print("-=" * 20)