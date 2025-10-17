Numero = int(input("Digite um numero inteiro:"))
Base = int(input ("Escolha uma Opção para conversão \n 1.Binario \n 2.Octal \n 3.Hexadecimal \n Opção:" ))

if Base >= 4:
    print("Opção invalida. Tente novamente.")

elif Base == 1:
    print("Numero {} em Binario e {}".format(Numero, bin(Numero)[2:]))
elif Base == 2:
    print("Numero {} em Octal  e {}".format(Numero, oct(Numero)[2:]))
elif Base == 3:
    print("Numero {} em Hexadecimal e {}".format(Numero, hex(Numero)[2:]))
