aluno = dict()
for v in range (0,1):
    aluno['nome'] = input('Nome: ')
    aluno['media'] = float(input(f'Média de {aluno['nome']} é : '))
print(f'O nome é igual á {aluno['nome']}')
print(f'A média é {aluno['media']}')
print('A situação do aluno é: ',end= '')
if aluno['media']>= 7 :
    print('\033[1;32mAprovado!!',end='')
else:
    print('\033[1;31mReprovado!!',end= '')