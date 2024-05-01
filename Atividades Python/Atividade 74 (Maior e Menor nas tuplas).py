import random
valores = (random.randint(1,10),random.randint (0,10),random.randint (0,10),random.randint (0,10),random.randint (0,10))
print('Os valores sortiados foram : ',end = '')
for c in valores :
    print(c ,'' ,end='')
print(f'\nO maior valor sortido foi : {max(valores)}')
print(f'O menor valor sortido foi : {min(valores)}')