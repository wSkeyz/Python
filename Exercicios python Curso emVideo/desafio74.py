from random import randint
valores = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print (valores)
maior = valores[0]
menor = valores[0]
for v in valores[1:]:
    if v > maior:
        maior = v
    if v < menor:
        menor = v
print(f"Menor valor {menor}, maior valor {maior}")