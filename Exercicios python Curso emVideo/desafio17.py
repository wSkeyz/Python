import math
co = float(input('Digite o cateto oposto: '))
ca = float(input("digite o caceto adjacente:"))
math.hypot(co, ca)
print("a hipotenusa de {} e {} vai ser {:.2f}.".format(co, ca, math.hypot(co, ca)))