from time import sleep
n1 = int(input('Escolha um número: '))
print('\033[1;33m ANALIZANDO',end= ' ')
print('.',end= ' ')
sleep (0.5)
print('.',end= ' ')
sleep (0.5)
print('.')
sleep (0.5)
if n1 % 2 == 0 :
    print('\033[1;34m {} é um número PAR!!'.format(n1))
else:
    print('\033[1;35m {} é um número ÍMPAR!!'.format(n1))

