import random
from time import sleep
print('='*30)
print('MEGA CENA'.center(30))
print('='*30)
megacena = list(range(1,61))
quant = int(input('Quantos jogos deseja fazer: '))
for a in range(1,quant+1):
    print(f'Jogo {a}: ',end = '')
    random.shuffle(megacena)
    print(f'{megacena[:6]}')
    sleep(0.5)
    del(megacena[:6])