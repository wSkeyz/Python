Peso = float(input("Qual o seu peso? (Kg)"))
Altura = float(input("Qual a sua altura? (m)"))
IMC = Peso / (Altura ** 2)
if IMC < 18.5:
    print("Seu IMC e de {:.1f}, voce esta abaixo do peso ideal.".format(IMC))
elif IMC >= 18.5 and IMC < 25:
    print("Seu IMC e de {:.1f}, voce esta no peso ideal.".format(IMC))
elif IMC >= 25 and IMC < 30:
    print("Seu IMC e de {:.1f}, voce esta com sobrepeso.".format(IMC))
elif IMC >= 30 and IMC < 40:
    print("Seu IMC e de {:.1f}, voce esta com obesidade.".format(IMC))
else:
    print("Seu IMC e de {:.1f}, voce esta com obesidade morbida.".format(IMC))