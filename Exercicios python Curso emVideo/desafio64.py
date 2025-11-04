numero = 0
soma = 0
digitados = -1
while numero < 999:
    soma = soma + numero
    digitados = digitados + 1
    numero = int(input("Digite um numero:"))
print("A soma dos numeros digitados e de {}, e foram digitados {} numeros".format(soma, digitados))