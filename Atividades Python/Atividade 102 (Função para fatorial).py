def fatorial(fct,show=True):
    """
    Calcular o Fatorial de um número
    :param fct: O número que vai ser calculado
    :param show: (opcional) Verifica se o vai ou não aver a conta
    :return: O valor do fatorial do número
    """
    mult = 1
    print('='*30)
    for c in range(fct,0,-1):
        mult *= c
        if show:
            print(f'{c}', end='')
            if c>1:
                print(' X ', end='')
            else:
                print(' = ',end= '')
    return mult


f = int(input('Fatorial: '))
print(fatorial(f))
help(fatorial)