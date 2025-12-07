valore = []
while True:
    valor = int(input("Digite um valor:"))
    if valor in valore:
        print("Valor duplicado! Não vou adicionar...")
    else:
        print("Valor adicionado com sucesso...")
        valore.append(valor)
    continuar = str(input("Deseja continuar? [S/N]")).strip().upper()[0]
    if continuar == "N":
        break
valore.sort()
print(f"Valores digitados em ordem foram {valore}")
    