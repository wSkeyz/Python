
maior_idade_homem = 0
nome_homem_velho = ''
soma_idades = 0
contador_mulheres_menos_20 = 0

for i in range(1, 5):
    nome = input("Digite o nome da {}ª pessoa: ".format(i)).strip()
    idade = int(input("Digite a idade da pessoa: "))
    sexo = input("Digite o Sexo [M/F]: ").strip().upper()

    soma_idades += idade

    if sexo == 'M':
        if idade > maior_idade_homem:
            maior_idade_homem = idade
            nome_homem_velho = nome
    elif sexo == 'F':
        if idade < 20:
            contador_mulheres_menos_20 += 1

media_idade = soma_idades / 4
print("A média de idade do grupo é de {:.1f} anos".format(media_idade))
if nome_homem_velho:
    print("O homem mais velho tem {} anos e se chama {}".format(maior_idade_homem, nome_homem_velho))
else:
    print("Não foi informado nenhum homem no grupo.")
print("Ao todo são {} mulheres com menos de 20 anos".format(contador_mulheres_menos_20))
