from menu.principal import *
def a_existe(n):
    try:
        a = open(n,'rt')
        a.close()
    except:
        return
    else:
        return True



def a_nexiste(n):
    try:
        a = open(n,'wt+')
        a.close()
    except:
        print(color('Algo deu errado,na criação do arquivo',1))
    else:
        print(color(f'Arquivo {n} criando com sucesso!!!',5))


def lera(n):
    try:
        a = open(n,'rt')
    except:
        print(color('Erro, ao ler o arquivo',1))
    else:
        l('PESSOAS CADASTRADAS',False)
        print(a.read())
    finally:
        a.close()


def cadastro(arq,n='<Desconhecido>',i=0):
    try:
        a = open(arq,'at')
    except:
        print(color('Erro, ao ler o arquivo',1))
    else:
        try:
            a.write(f'\n{n};{i}')
        except:
            print(color('Erro ao adicionar dado',1))
        else:
            print(color(f'Registro feito, {n} foi adiconado com sucesso!!',6))
            a.close()


