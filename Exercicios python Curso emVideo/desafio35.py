print("digite tres numeros e descubra se eles formam um triangulo ou não.")
r1 = int(input("digite o primeiro lado do triangulo:"))
r2 = int(input("digite o segundo lado do triangulo:"))
r3 = int(input("digite o terceiro lado do trinagulo:"))
if r1 + r2 > r3 or r1 + r3 > r2 or r2 + r3 > r1:
    print("os lados {}, {}, {}.\n Formam um triangulo.".format(r1, r2, r3))
else:
    print("os lados {}, {}, {}.\nInfelizmente não conseguem formar um triangulo.".format(r1, r2, r3))