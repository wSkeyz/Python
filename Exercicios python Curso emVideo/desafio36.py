# Se o valor da prestação da casa for maior que 30% do salario da pessoa, ela nao vai poder comprar a casa.
Casa = int (input("Qual Valor da casa?"))
Salario = int (input("Qual o Seu salario?"))
Parcelas = int (input("Quantas parcelas?"))
Parcelasf = Casa / Parcelas
if Parcelasf > (Salario * 0.30):
    print("Infelizmente a casa e muito cara para seu poder de compra atual, com base no seu salario de {}, as parcelas ficaram em {}".format(Salario, Parcelasf))
elif Parcelasf <= (Salario * 30):
    print("Sua Casa pode ser parceladas em {} Vezes, e o valor das parcelas sera de {:.2f}R$, Com base em seu salario {}R$ Aprovamos sua compra dessa casa.".format(Parcelas, Parcelasf, Salario))

