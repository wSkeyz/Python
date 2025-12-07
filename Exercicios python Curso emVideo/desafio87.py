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
soma_pares = 0
soma_terceira_coluna = 0
soma_terceira_coluna = matriz[0][2] + matriz[1][2] + matriz[2][2]
maior_segunda_linha = max(matriz[1])    
for i in range (3):
    for j in range (3):
        if matriz[i][j] % 2 == 0:
            soma_pares += matriz[i][j]
print(f"A soma dos valores pares é {soma_pares}")
print(f"A soma dos valores da terceira coluna é {soma_terceira_coluna}")
print(f"O maior valor da segunda linha é {maior_segunda_linha}")