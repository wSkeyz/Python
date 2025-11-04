import random
aleatorio = random.randint(1, 10)
#jogada = 0 # input(int("Digite um número entre 0 e 10:"))
tentativas = 0
while True:
    jogada = (input("Digite um número entre 1 e 10: "))
    if jogada == "":
        print("Por favor, digite um número válido.")
        continue
    jogada = int(jogada)
    tentativas = tentativas + 1 
    if jogada == aleatorio:
        break
    else:
        print("Número incorreto. Tente novamente.")
print("Parabéns! Você acertou o número {} com {} tentativas.".format(aleatorio, jogada))