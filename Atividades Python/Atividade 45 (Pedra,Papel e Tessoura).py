import random
from time import sleep
print('\033[4mBEM VINDO AO GAME JO-KEN-PO\033[m')
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESSOURA''')
opcao = int(input('Escolha sua opcão: '))
if opcao in (0,1,2) :
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO !!!')
    lista = ('Pedra', 'Papel', 'Tessoura')
    com = random.randint(0, 2)
    print('/' * 22)
    print('Computador jogou {}'.format(lista[com]))
    print('Jogador jogou {}'.format(lista[opcao]))
    print('/' * 22)
    if com == 0 and opcao == 2 :
        print('\033[1;34mCOMPUTADOR VENCEU!')
    elif com == 0 and opcao == 1 :
        print('\033[1;32mJOGADOR VENCEU!!')
    elif com == 1 and opcao == 0 :
        print('\033[1;34mCOMPUTADOR VENCEU!')
    elif com == 1 and opcao == 2 :
        print('\033[1;32mJOGADOR VENCEU!!')
    elif com == 2 and opcao == 1 :
        print('\033[1;32mJOGADOR VENCEU!!')
    elif com == 2 and opcao == 0 :
        print('\033[1;34mCOMPUTADOR VENCEU!')
    elif com == opcao :
        print('\033[1;37mEMPATE!!')
else :
    print('\033[1;31mTente novamente, escolha um número de 0 á 2')