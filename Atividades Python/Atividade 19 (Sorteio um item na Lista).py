import random
n1 = input('Insira o primeiro aluno: ')
n2 = input('Insira o segundo aluno: ')
n3 = input('Insira o terceiro aluno: ')
n4 = input('Insira o quarto aluno: ')
lista = [n1,n2,n3,n4]
escolha = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolha))
