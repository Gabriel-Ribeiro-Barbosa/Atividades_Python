import random

def color(t,n=0):
    print(f'\033[1;3{n}m{t}\033[m')


def gerar(lista):
    com = random.choice(lista)
    return com


def face(n):
    print('='*20)
    print(n.center(20))
    print('='*20)


lista = ['palavra','hoje','texto','cafe','galo']
