numero = int(input("Digite um numero para saber seu fatorial:"))
contador = 1
fatorial = 1
while contador <= numero:
    fatorial = fatorial * contador
    contador += 1
print("O fatorial de {} é {}".format(numero, fatorial))
