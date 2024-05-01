from time import sleep
def color(n,c=0):
    return f'\033[1;3{c}m{n}\033[m'

def l(n,c=False):
    print('-'*30)
    print(n.center(30))
    print('-'*30)
    if c:
        print("""[1] VER PESSOAS CADASTRADAS
[2] ADICIONAR UM CADASTRO
[3] SAIR DO PROGRAMA""")
        print('-' * 30)


def dado(n):
    while True:
        try:
            dado = int(input(n))
        except (ValueError,NameError):
            print(color('Erro no dado informado, por favor digite um número valido',1))
        except KeyboardInterrupt:
            print(color('\nPor favor,informe uma opção!!',1))
        else:
            break
    return dado


def tempo(t=0.5):
    for c in range(0,3):
        print('.',end= '')
        sleep(t)
    print()


def leiaInt(num):
    while True:
        try:
            n = int(input(f'\033[m{num}'))
        except (NameError,ValueError):
            print(color('Erro no dado digitado, digite um número inteiro',1))
        except KeyboardInterrupt:
            print(color('Erro, usuário não informou o dado',1))
        else:
            break
    return n


def leiaStr(n='<desconhecido>'):
    while True:
        n = str(input(f'\033[m{n}'))
        if not n.isalpha:
            print(color('Erro no dado digitado, digite um número inteiro',1))
        else:
            break





