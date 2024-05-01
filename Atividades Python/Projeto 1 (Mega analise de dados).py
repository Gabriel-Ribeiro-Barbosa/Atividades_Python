from time import sleep
lista = []
pri = []
maior = menor = mulher = homem = cont = 0
print('Seja bem vindo ao programa de analise de dados: ')
comecar = ''
while comecar == '' or comecar not in 'SN':
    comecar = input('\033[1;35mDeseja começar o programa?[S/N]: ').strip().upper()
    if comecar == 'N':
        print('Ok,volte quando quizer...')
    if comecar not in 'SN':
        print('\033[1;31mOpçaõ inválida')
    if comecar == 'S':
        print('Ok, programa iniciando',end='')
        for c in range(0,3):
            print('.',end= '')
            sleep(0.5)
        print('\033[m')
        while True:
            print('='*20)
            print(f'PESSOA {cont}'.center(20))
            print('='*20)
            nome = input('Digite o nome da pessoa: ')
            cont+= 1
            lista.append(nome)
            peso = float(input('Digite o peso da pessoa Kg'))
            lista.append(peso)
            sexo = ''
            while sexo == '' or sexo not in 'MF':
                sexo = input('\033[mDigite o sexo[M/F]: ').strip().upper()
                if sexo == 'M':
                    lista.append(sexo)
                    homem += 1
                elif sexo == 'F':
                    lista.append(sexo)
                    mulher += 1
                elif sexo not in 'MF':
                    print('\033[1;31mOpção inválida\033[m')
            if not pri :
                maior = lista[1]
                menor = lista[1]
            pri.append(lista[:])
            for p in pri:
                if p[1] > maior:
                    maior = p[1]
                elif p[1] < menor:
                    menor = p[1]
            lista.clear()
            add = input('Quer continuar[S/N]: ').strip().upper()
            while add not in 'SN':
                add = input('\033[1;31mTente Novamnete,quer continuar[S/N]: \033[m').strip().upper()
            if add == 'N':
                break
        print(f'Foram lidas {len(pri)} pesssoas,sendo {mulher} mulheres e {homem} homens')
        print(f'O maior peso foi de {maior} de: ',end = '')
        for name in pri:
            if name[1] == maior:
                print(f'{name[0]}',end = '')
        print(f'\nO menor peso foi de {menor} de: ',end= '')
        for name in pri:
            if name [1] == menor:
                print(f'{name[0]}',end = '')
        print()
        print('Essa é uma tabela com seus dados: ')
        print('=-'*20)
        print(f'{'N°':<8}{'NOME':<10}{'SEXO':<8}{'PESO':>5}')
        for c,v in enumerate(pri):
            print(f'{c:<8}{v[0]:<10}{v[2]:<8}{v[1]:>5}',end= '')
            print()
        print('=-'*20)
        while True :
            termo = int(input('Qual cadastro deseja ver:[999 para sair] '))
            if termo == 999:
                break
            if termo <= len(pri) - 1:
                print(f'Os dados de {pri[termo][0]} são:')
                print('=-'*20)
                print(f'{'N°':<8}{'NOME':<10}{'SEXO':<8}{'PESO':>5}')
                print(f'{termo:<8}{pri[termo][0]:<10}{pri[termo][2]:<8}{pri[termo][1]:>5}',end= '')
                print()
                print('=-'*20)
            else:
                print('\033[1;31mOpção inválida\033[m')
print('Finalizando',end='')
for c in range(0, 3):
    print('.', end='')
    sleep(0.5)
print()
print('\033[1;32mPrograma finalizado,volte sempre!!!')