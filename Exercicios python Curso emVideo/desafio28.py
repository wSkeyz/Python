import random
pensar = random.randint(1, 5)
print("Pensando.... em um numero de 1 a 5")
resposta = int (input ("digite um numero de 1 a 5:"))
if resposta == pensar:
    print("Parabens, voce acertou na mega sena")
elif resposta <= 6 or resposta <= 0:
    print("voce colocou um numero invalido.")
else:
    print("voce errrou!!, tente novamente e teste sua sorte")
print("A final o numero pensando foi {}".format(pensar))