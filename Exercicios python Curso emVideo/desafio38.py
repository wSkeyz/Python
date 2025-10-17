Numero1 = int(input("Digite um numero qualquer inteiro:"))
Numero2 = int(input("Digite outro numero qualquer inteiro:"))
if Numero1 > Numero2:
    print("O numero {} e maior que o numero {}".format(Numero1, Numero2))
elif Numero2 > Numero1:
    print("O numero {} e maior que o numero {}".format(Numero2, Numero1))
elif Numero2 == Numero1:
    print("Os numeros {} e {} sao iguais".format(Numero1, Numero2))
