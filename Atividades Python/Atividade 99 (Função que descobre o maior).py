from random import randint
from time import sleep
def linha(esc):
    print('='*len(esc))
    print(esc)
    print('='*len(esc))
def maior(num):
    linha(f'Analisando os números gerados...')
    lista = []
    if num == 0:
        print('0 ',end= '')
        sleep(0.5)
        print(f'Foram informados 1 valores sendo 0 o maior deles', end='')
        print()
    else:
        for c in range(num):
            com = randint(1,100)
            lista.append(com)
        for c in lista:
            print(f'{c} ',end = '')
            sleep(0.5)
        print(f'Foram informados {len(lista)} valores sendo {max(lista)} o maior deles', end='')
        print()
        sleep(0.5)


maior(6)
maior(3)
maior(2)
maior(1)
maior(0)