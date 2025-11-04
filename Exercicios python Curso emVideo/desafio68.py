from time import sleep
from random import randint
vitoria = total = jogador = 0
while True:
    print("-=" * 20)
    print("Jogo do par ou impar")
    print("iniciando...")
    sleep(1)
    print("-=" * 20)
    jogador = int(input("Qual seu numero desejado?"))
    escolha = str(input("Deseja jogar par ou impar? [P/I]")).strip().upper()[0]
    computador = randint(0, 10)
    total = jogador + computador
    if escolha == "P":
        if total % 2 == 0:
            print(f"Voce jogou {jogador} e o computador jogou {computador}, o total foi de {total} que e par")
            print("-=" * 20)
            sleep(1)
            print("Voce venceu!")
            print("-=" * 20)
            vitoria += 1
        else:
            print(f"voce jogou {jogador} e o computador jogou {computador}, o total foi de {total} que e impar")
            print("-=" * 20)
            sleep(1)
            print("Voce perdeu!")
            print("-=" * 20)
            break
    if escolha == "I":
        if  total % 2 != 0:
            print(f"voce jogou {jogador} e o computador jogou {computador}, o total foi de {total} que e impar")
            print("-=" * 20)
            sleep(1)
            print("Voce venceu!")
            print("-=" * 20)
            vitoria += 1
        else:
            print(f"Voce jogou {jogador} e o computador jogou {computador}, o total foi de {total} que e par")
            print("-=" * 20)
            sleep(1)
            print("Voce perdeu!")
            print("-=" * 20)
            break
            
print(f"Sua Total de vitorias foi de {vitoria}")