import random
i = 1
cont = int(input("Quantos alunos deseja sortear: "))
name = []
while i <= cont:
    name.append((input("Digite o nome do Aluno: ")))
    i +=1
print('O sorteado é {}'.format(random.choice(name)))