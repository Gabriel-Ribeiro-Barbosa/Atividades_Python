from time import sleep
lista = []
while True :
    nome = input('Nome do aluno: ').strip()
    nota1 = float(input('Nota 1: '))
    while nota1 > 10 :
        nota1 = float(input('\033[1;31mDigite um número de 0 a 10,nota 1: \033[m'))
    nota2 = float(input('Nota 2: '))
    while nota2 >10 :
        nota2 = float(input('\033[1;31mDigite um número de 0 a 10 ,nota 2: \033[m'))
    media = (nota1+nota2)/2
    lista.append([nome,[nota1,nota2],media])
    add = input('Quer continuar[S/N]: ').strip().upper()
    while add not in 'SN' :
        add = input('\033[1;31mTente novamente,quer continuar[S/N]: \033[m').strip().upper()
    if add == 'N' :
        break
print('='*22)
print(f'{'N°':<4}{'NOME':<10}{'MÉDIA':>8}')
print('='*22)
for numero, valor in enumerate(lista):
    print(f'{numero:<4}',end='')
    print(f'{valor[0]:<10}',end ='')
    print(f'{valor[2]:>8}',end='')
    print()
print('='*22)
while True:
    aluno = int(input('Deseja ver a nota de qual aluno[999 para sair]: '))
    if aluno == 999:
        break
    if aluno <= len(lista) - 1 :
        print(f'\033[1;33m{lista[aluno][0]} tirou as notas {lista[aluno][1]}\033[m')
print(f'Finalizando programa',end = '')
for c in range(0,3) :
    print(f'.',end='')
    sleep(0.5)
print('\nPrograma finalizado!!')