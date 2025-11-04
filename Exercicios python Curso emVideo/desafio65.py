numero = 0
media = 0 
maior = 0
menor = 0
soma = 0
sair = ("S/N").upper()
contador = 0
while True:
    numero = int(input("digite um numero:"))
    soma += numero
    print("Quer continuar?")
    sair = input("[S/N]:").upper()
    if contador == 0:
        maior = numero
        menor = numero
    contador = contador + 1
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    if sair == "N":
        break
media = soma / contador
print("A media dos numeros digitados e de {}, o maior e {} e o menor e {}".format(media, maior, menor))