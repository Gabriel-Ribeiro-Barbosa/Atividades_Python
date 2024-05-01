def leiaint(n):
    while True:
        try:
            num = int(input(f'\033[m{n}'))
        except (ValueError,NameError):
            print('\033[1;31mErro no dado informado, por favor digite um número inteiro')
        except KeyboardInterrupt:
            print('\033[1;31m\nO usuário preferiu não informar o valor\033[m')
            return 0
        else:
            break
    return num


def leiafloat(n):
    while True:
        try:
            num = float(input(f'\033[m{n}'))
        except (ValueError,NameError):
            print('\033[1;31mErro no dado informado, por favor digite um número real')
        except KeyboardInterrupt:
            print('\033[1;31m\nO usuário preferiu não informar o valor\033[m')
            return 0
        else:
            break
    return num


i = leiaint('Digite um valor inteiro: ')
r = leiafloat('Digite um valor real: ')
print(f'O número inteiro digitado foi {i} e o número real foi {r}')

