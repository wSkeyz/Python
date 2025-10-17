Produto = int(input("Digite o valor do produto:"))
Pagamento = int(input("""Escolha a forma de pagamento:
[1] À vista dinheiro/cheque (10% de desconto
[2] À vista no cartão (5% de desconto
[3] Em até 2x no cartão (preço normal
[4] 3x ou mais no cartão (20% de juros
Digite a opção desejada:"""))
if Pagamento == 1:
    Desconto = Produto - (Produto * 0.10)
    print("O valor do produto com 10% de desconto é de {:.2f}R$".format(Desconto))
elif Pagamento == 2:
    Desconto = Produto - (Produto * 0.05)
    print("O valor do produto com 5% de desconto é de {:.2f}R$".format(Desconto))
elif Pagamento == 3:
    print("O valor do produto é de {:.2f}R$, e pode ser parcelado em até 2x sem juros.".format(Produto))
elif Pagamento == 4:
    Juros = Produto + (Produto * 0.20)
    print("O valor do produto com 20% de juros é de {:.2f}R$".format(Juros))
