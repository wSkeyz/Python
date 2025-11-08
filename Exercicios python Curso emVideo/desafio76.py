listagem = ("Caneta", 1, "borracha", 2.50)
c = 0
a = 0
for i in listagem[0 + a:]:
    print(listagem[0 + c],"." * 5,"R$",listagem[1 + c::2 + c], "\n")
    c += 1
    a += 2
