from time import sleep
primeiro = int(input('Qual o primeiro termo: '))
segundo = int(input('Qual o segundo termo: '))
print('''Escolha sua opção:
[1] somar
[2] multiplicar
[3] maior 
[4] novos números
[5] sair do programa''')
opcao = int(input('Qual a sua opção: '))
while opcao != 5 :
    if opcao == 1 :
        print('{} + {} = {}'.format(primeiro,segundo,primeiro+segundo))
        opcao = int(input('Qual a sua opção: '))
    elif opcao == 2 :
        print('{} X {} = {}'.format(primeiro, segundo, primeiro * segundo))
        opcao = int(input('Qual a sua opção: '))
    elif opcao == 3 and primeiro> segundo:
        print('O maior é {}'.format(primeiro))
        opcao = int(input('Qual a sua opção: '))
    elif opcao == 3 and segundo > primeiro :
        print('O maior é {}'.format(segundo))
        opcao = int(input('Qual a sua opção: '))
    elif opcao == 4 :
        print('Escolha seus novos números: ')
        primeiro = int(input('Qual o primeiro termo: '))
        segundo = int(input('Qual o segundo termo: '))
        opcao = int(input('Qual a sua opção: '))
    else :
        opcao = int(input('Ouve um erro,qual a sua opção: '))
print('Finalizando',end= '')
sleep(0.5)
print('.',end = ' ')
sleep(0.5)
print('.',end = ' ')
sleep(0.5)
print('.',end = ' ')
print('\nPrograma finalizado,volte sempre!!')