lista = []
menor = 0
maior = 0
posicao = 0
posicao2 = 0
for v in range(0,5):
    lista.append(int(input(f"Digite um Numero para a lista {v}: ")))
    if v == 0:
        menor = maior = lista[v]
    if lista[v] < menor:
        menor = lista[v]
        posicao = v
    if lista[v] > maior:
        maior = lista[v]
        psoicao2 = v

print(lista, maior, psoicao2, menor, posicao)