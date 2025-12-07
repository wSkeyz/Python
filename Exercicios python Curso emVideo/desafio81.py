lista = []
while True:
    valor = int(input("Digite um valor ou 999 para parar:"))
    if valor == 999:
        break
    else:
        lista.append(valor)
print(f"Foram digitados {len.lista} valores")
print(f"A lista em ordem decrescente é {sorted(lista, reverse=True)}")
print(f"O valor 5 faz parte da lista" if 5 in lista else "O valor 5 não foi encontrado na lista")
