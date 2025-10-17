import random
import time

Escolha = int(input('''Suas opções:
Pedra (1)
Papel (2)
Tesoura (3)
Qual é a sua jogada? '''))

Computador = random.randint(1, 3)
time.sleep(1)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PÔ!!!')
time.sleep(1)
if  Escolha == 1:
    Jogada = 'Pedra'
elif Escolha == 2:
    Jogada = 'Papel'
else:
    Jogada = 'Tesoura'

print("===============================================" 
          "Resultado da partida entre voce e o computador" 
          "===============================================")
time.sleep(2)
if Escolha == 1:
    if Computador == 1:
        print("""====================================================
                 Computador jogou Pedra e voce jogou {}.Empate! 
                 ====================================================""").format(Jogada)
    elif Computador == 2:
        print("""====================================================
                 Computador jogou Papel e voce jogou {}.Você perdeu!
                 ====================================================""".format(Jogada))
    else:
        print("""====================================================
                 Computador jogou Tesoura e voce jogou {}. Você ganhou!
                 ====================================================""".format(Jogada))
elif Escolha == 2: 
    if Computador == 1:
        print("""====================================================
                 Computador jogou Pedra e voce jogou {}.Você ganhou!
                 ====================================================""".format(Jogada))
    elif Computador == 2:
        print("""==================================================== 
                 Computador jogou Papel e voce jogou {}.Empate!
                 ====================================================""".format(Jogada))
    else:
        print("""====================================================
                 Computador jogou Tesoura e voce jogou {}.Você perdeu!              
                 ====================================================""".format(Jogada))
elif Escolha == 3:
    if Computador == 1:
        print("""====================================================
                 Computador jogou Pedra e voce jogou {}.Você perdeu!
                 ====================================================""".format(Jogada))
    elif Computador == 2:
        print("""====================================================
                 Computador jogou Papel e voce jogou {}.Você ganhou!
                 ====================================================""".format(Jogada))
    else:
        print("""====================================================
                 Computador jogou Tesoura e voce jogou {}.Empate!
                 ====================================================""".format(Jogada))