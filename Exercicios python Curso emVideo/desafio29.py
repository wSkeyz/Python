velocidade = int(input("digite a velocidade do carro em km:"))
if velocidade <= 80:
    print("Voce esta dentro do limite de velocidade permitido. ")
else:
    print("voce esta acima do limite de velocidade permitido,\nSera multado em {}R$.\ndiriga em 80 km/h ou menos.".format((velocidade - 80)* 7))
