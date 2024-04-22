import random
i = 1
cont = int(input("Quantos alunos vão apresentar o trabalho?: "))
name = []
while i <= cont:
    name.append((input("Digite o nome do Aluno: ")))
    i +=1
print('A ordem de apresentação é {}'.format(random.sample(name, cont)))
