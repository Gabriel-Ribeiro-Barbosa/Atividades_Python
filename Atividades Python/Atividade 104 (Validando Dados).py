def leiaInt(num):
    while True:
        n = str(input(f'\033[m{num}')).strip()
        if n.isnumeric():
            return n
            break
        else:
            print('\033[1;31mErro,digite um número')


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')