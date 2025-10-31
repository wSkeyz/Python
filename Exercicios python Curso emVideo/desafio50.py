soma = 0
for c in range(0, 6):
    pares = int(input("Digite um numero para ver a soma de 0 ate o numero digitado somando apenas os pares:"))
    if pares % 2 == 0: 
        soma = soma + pares
    else:
        continue
print("A soma dos numeros pares é {}".format(soma))