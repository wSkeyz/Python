numeros = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", 
"dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte",)
escolha = int(input("Escolha um numero de 0 a 20:"))
while True:
    if escolha < 0 or escolha > 20:
        escolha = int(input("Digite um numero invalido! 0 a 20:"))
    else:
        break
print(f"Voce digitou o numero {numeros[escolha]}")