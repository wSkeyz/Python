tabuada = int(input("Digite um numero para saber sua tabuada:"))
for c in range(0, 9):
    print("{} x {} = {}".format(tabuada, c+1, tabuada * (c+1)))