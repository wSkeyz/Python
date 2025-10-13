ano = int(input("digite um ano para saber se ele e bissexto ou nao:"))
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print("o ano de {} e bissexto".format(ano))
else: 
    print("o ano de {} nao e bissexto".format(ano))