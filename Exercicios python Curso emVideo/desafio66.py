soma = contador = valor = 0
while True:
    valor = int(input("Digite um numero:"))
    if valor == 999:
        break
    contador = contador + 1
   # valor = int(input("Digite um numero:"))
    soma = valor + soma
print(f"a soma dos {contador} numeros digitados e de {soma}.")