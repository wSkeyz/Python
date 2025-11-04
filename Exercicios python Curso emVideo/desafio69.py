maior = 0
homens = 0
idade = 0
mulheres = 0
while True:
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]
    
    while sexo not in ("M", "F"):
        print("Sexo invalido.")
        sexo = str(input("Digite o sexo novamente [M/F]: ")).strip().upper()[0]
    
    if idade >= 18:
        maior += 1
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade < 20:
        mulheres += 1
    print("Quer continuar a cadastrando pessoas?")

    continuar = str(input("S/N: ")).strip().upper()[0]
    if continuar == "N":
        break
print(f"temos {maior} pessoas maior de 18 anos")
print(f"Foram cadastrados {homens} Homens")
print(f"{mulheres} Mulheres tem menos de 20 anos")