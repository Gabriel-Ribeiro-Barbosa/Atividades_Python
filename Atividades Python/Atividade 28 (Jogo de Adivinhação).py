from time import sleep
import random
print('\033[1;34m -=-'*20)
print('\033[1;35m Vou pensar em um número de 0 á 5,tente adivinhar...')
print('\033[1;34m -=-'*20)
n = int(input('\033[1;36m Qual é o seu chute: '))
print('CARREGANDO')
print('.')
sleep(0.5)
print('.')
sleep(0.5)
print('.')
sleep(0.5)
lista = [0,1,2,3,4,5]
escolha = random.choice(lista)
if n not in lista   :
    print('\033[1;31m Tente novamente, escolha um número de 0 á 5')
else :
    if n == escolha :
        print('\033[1;35m Jogador escolheu {} e o computador escolheu {} logo...'.format(n, escolha))
        print('\033[1;32m Você ganhou!!!')
    else :
        print('\033[1;37m O computador ganhou.Tente novamente')

