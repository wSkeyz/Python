numeros = []
pares = []
impares = []

while True:
    numero = int(input("Digite um número: "))
    numeros.append(numero)
    
    continuar = input("Deseja continuar? [S/N]: ").strip().upper()
    if continuar == "N":
        break

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f"\nNúmeros digitados: {numeros}")
print(f"Valores pares: {pares}")
print(f"Valores ímpares: {impares}")