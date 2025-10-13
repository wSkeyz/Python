n1 = int(input("digite primeiro numero:"))
n2 = int(input("digite segundo numero:"))
n3 = int(input("digite o terceiro numero:"))
if n1 < n2 and n1 < n3:
    print("o menor numero e {}".format(n1))
elif n2 < n1 and n2 < n3:
    print("o menor numero e {}".format(n2))
else:
    print("o menor numero e {}".format(n3))
if n1 > n2 and n1 > n3:
    print("o maior numero e {}".format(n1))
elif n2 > n1 and n2 > n3:
    print("o maior numero e {}".format(n2))
else:
    print("o maior numeero e {}".format(n3))
print ("de todos numeros digitados a sequencia a cima e do menor e o maior numero digitados.")
        