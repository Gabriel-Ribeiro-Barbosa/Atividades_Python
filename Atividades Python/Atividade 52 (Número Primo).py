n = int(input('Digite um número: '))
tot = 0
for c in range (1,n+1) :
    if n % c == 0 :
        print('\033[1;32m',end = ' ')
        tot += 1
    else :
        print('\033[1;31m',end = ' ')
    print(c,'\033[1;37m->',end = ' ')
print('FIM',end = ' ')
print('\nO número {} foi divisível {} vezes, sendo assim esse número:'.format(n,tot))
if tot == 2:
    print('\033[1;32mÉ um número PRIMO')
else :
     print('\033[1;31mNÃO é um número primo')