print("digite tres numeros e descubra se eles formam um triangulo ou não.")
r1 = int(input("digite o primeiro lado do triangulo:"))
r2 = int(input("digite o segundo lado do triangulo:"))
r3 = int(input("digite o terceiro lado do trinagulo:"))
if r1 == r2 == r3:
    print("Sera formado um triangulo EQUILÁTERO.")
elif r1 != r2 != r3 != r1:
    print("Sera formado um triangulo ESCALENO.")
else:
    print("Sera formado um triangulo ISÓSCELES.")