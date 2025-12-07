pessoas = []
dados = []
maior = menor = 0
while True:
    dados.append(str(input("Nome:")))
    dados.append(float(input("Peso:")))
    pessoas.append(dados[:])
    dados.clear()
    continuar = str(input("Deseja continuar? [S/N]")).strip().upper()[0]
    if continuar == "N":
        break
    for p in pessoas:
        if p[1] > maior:
            maior = p[1]
        if menor == 0:
            menor = p[1]
        if p[1] < menor:
            menor = p[1]
print("-="*20)
print(f"Foram cadastradas  {len(pessoas)} pessoas!")
print("Pessoas com peso menor de 70kg: ", end="")
menores_70 = [p[0] for p in pessoas if p[1] < 70]
print(menores_70 if menores_70 else "Nenhuma")
print("-="*20)
print("Pessoas com peso maior de 100kg: ", end="")
maiores_100 = [p[0] for p in pessoas if p[1] > 100]
print(maiores_100 if maiores_100 else "Nenhuma")
print("-="*20)
print(f"O menor peso foi de {menor}Kg.",  end="")
print("-="*20)
print(f"O maior peso foi de {maior}Kg. Peso de ", end="")
print("-="*20)