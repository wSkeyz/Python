from time import sleep
numero1 = int(input("Digite o 1 numero:"))
numero2 = int(input("digite o 2 numero:"))
opçao = 0
print("""Digite 
    [1] Para somar os numeros.
    [2] Para mutiplicar os numeros.
    [3] Para saber qual e o maior numero.
    [4] Para digitar novos numeros.
    [5] Para sair do programa.""") 
while opçao != 5:
    opçao = int(input("Digite a sua opção:"))
    if opçao == 1:
        print("A soma entre {} + `{}, e de {}".format(numero1, numero2, numero1 + numero2))
    if opçao == 2:
        print("A mutiplicação entre {} x {}, e de {}".format(numero1, numero2, numero1 * numero2))
    if opçao == 3:
        if numero1 > numero2:
            print("O maior numero entre ambos digitados e o {}".format(numero1))
        else:
            print("O maior numero entre ambos digitados e o {}".format(numero2))
    if opçao == 4:
        numero1 = int(input("Digite o 1 numero novamente:"))
        numero2 = int(input("digite o 2 numero novamente:"))
        print("""Digite 
    [1] Para somar os numeros.
    [2] Para mutiplicar os numeros.
    [3] Para saber qual e o maior numero.
    [4] Para digitar novos numeros.
    [5] Para sair do programa.""") 
    if opçao == 5:
        sleep(2)
        print("""Finalizando...""")
    if opçao > 5:
        sleep(2)
        print("Opção invalida, tente novamente.")
        sleep(0.5)
        print("""Digite 
    [1] Para somar os numeros.
    [2] Para mutiplicar os numeros.
    [3] Para saber qual e o maior numero.
    [4] Para digitar novos numeros.
    [5] Para sair do programa.""") 