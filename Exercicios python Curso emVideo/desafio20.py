import random
aluno1 = str (input("digite o nome do 1 aluno:"))
aluno2 = str (input("digite o nome do 2 aluno:"))
aluno3 = str (input("digite o nome do 3 aluno:"))
aluno4 = str (input("digite o nome do 4 aluno:"))
alunos = aluno1, aluno2, aluno3, aluno4
print ("o aluno escolhi para apresentar foi \n{}".format(random.sample(alunos, k=4)))