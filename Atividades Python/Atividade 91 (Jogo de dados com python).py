from random import randint
from time import sleep
from operator import itemgetter
Jogador = {'Jogador 1 ' : randint(0,6),
'Jogador 2 ' : randint(0,6),
'Jogador 3 ' : randint(0,6),
'Jogador 4 ' : randint(0,6)}
for k,v in Jogador.items() :
    print(f'{k} tirou {v}')
    sleep(1)
print('-'*20)
print('Ordem de vencedores')
print('-'*20)
rankin = sorted(Jogador.items(),key =itemgetter(1), reverse= True)
for n,l in enumerate(rankin):
    print(f'{n+1}° ficou o {l[0]} que tirou {l[1]}')
    sleep(1)