soma = 0
barato = 0
caros_1000 = 0
barato2 = ""
while True:
    produto = input("Qual nome do produto? ")
    preco = float(input("Qual seu preço? "))
    soma = soma + preco
    if preco >= 1000:
        caros_1000 = caros_1000 + 1
    if barato == 0:
        barato = preco
        barato2 = produto
    if preco < barato:
        barato = preco
        barato2 = produto
    #barato2 = produto
    resposta = input("Quer continuar cadastrando produtos? [S/N]: ").strip().upper()[0]
    if resposta == "N":
        break
print(f"""Total gastos {soma}R$ em produtos\n {caros_1000} produtos que custam mais de 1000R$ \n o produto mais barato foi o {barato2}  """)
