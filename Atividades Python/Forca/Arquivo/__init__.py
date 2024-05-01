from Forca import *
from Forca.Palavras import *
def existe(n):
    try:
        a = open(n,'rt')
        a.close()
    except:
        return False
    else:
        return True


def nao(n):
    try:
        a = open(n,'wt+')
        a.close()
    except:
        color('Ouve um erro ao criar o arquivo',1)
    else:
        color(f'Arquivo {n} criado com sucesso!!',2)


def ler(n):
    try:
        a = open(n,'rt')
    except:
        color(f'Erro ao ler o arquivo!!',1)
    else:
        a.close()


def add(n):
    try:
        a = open(n,'at')
    except:
        color('Algo deu errado!!',1)
    else:
        a.close()




