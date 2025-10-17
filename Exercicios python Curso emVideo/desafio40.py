Nota1 = int(input("Digite a primeira nota do aluno:"))
Nota2 = int(input("Digite a segunda nota do aluno:"))
media = (Nota1 + Nota2) / 2
if media < 5:
    print("Reprovado")
elif media >= 5 and media < 6.9:
    print("Recuperação")
else:  
    print("Aprovado")