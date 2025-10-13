print ("qual a distancia da sua viagem em km?")
viagem = int (input("Distancia:"))
if viagem <= 200:
    print("o valor da sua passagem e {}R$".format(viagem * 0.50))
else:
    print("o valor da sua passagem e {}R$".format(viagem * 0.45))