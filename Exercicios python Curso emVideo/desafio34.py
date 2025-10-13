salario = float(input("digite o salario do funcionario:"))
if salario > 1250:
    print("o salario com o aumento sera de {}".format(salario + (salario * 10 / 100)))
else:
    print("O salario com o aumento sera de {}".format(salario + (salario * 15 / 100)))