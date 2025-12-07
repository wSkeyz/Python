lista = []
for c in range(0, 5):
    valor = (int(input(f"Digite um valor")))
    v = valor
    if c == 0:
        lista.insert(v, valor)
    if valor > lista[-1]:
            lista.append(valor)
    else:
            pos = 0
            while pos < len(lista):
                if valor <= lista[pos]:
                    lista.insert(pos, valor)
                    break
                pos += 1
print(f"Você digitou os valores {lista}")