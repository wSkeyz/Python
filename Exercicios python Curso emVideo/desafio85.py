numeros = []
pares = []
impares = []

for i in range(1, 8):
    numero = int(input(f"Digite o {i}º valor: "))
    numeros.append(numero)

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

pares.sort()
impares.sort()

print("-=" * 20)
print(f"Valores pares em ordem crescente: {pares}")
print(f"Valores ímpares em ordem crescente: {impares}")
print("-=" * 20)