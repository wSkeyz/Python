
n1 = int(input("Digite o primeiro valor:"))
n2 = int(input("Digite o segundo valor:"))
n3 = int(input("Digite o terceiro valor:"))
n4 = int(input("Digite o Ultimo valor:"))
valores = (n1, n2, n3, n4)
n9 = 0
pares = ()
posi_pares = ()
n3 = None
for i, v in enumerate(valores):
    if v == 9:
        n9 += 1
    if v % 2 == 0:
        pares = pares + (v, )
        posi_pares = posi_pares + (i + 1, )
    if v == 3 and n3 == None:
        n3 = {i + 1}
print(f'O valor 9 apareceu {n9} vezes.')
print(f'Valores pares: {pares}')
if n3 is None:
    print("Numero 3 não foi encontrado!")
else: 
    print(f"o numero 3 apareceu na posição {n3}")
