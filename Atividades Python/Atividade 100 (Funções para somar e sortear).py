from time import sleep
from random import randint
numeros = []
def lista(list):
    print(f'Sorteando 5 valores: ',end= '')
    for c in range(0,5):
        com = randint(0,20)
        sleep(0.5)
        numeros.append(com)
        print(f'{com} ',end= '')
    print()
def pares(par):
    somapar = 0
    for n in par:
        if n % 2 == 0:
            somapar+= n
    print(f'A soma par dos numeros: {numeros} é {somapar}')


lista(numeros)
pares(numeros)

