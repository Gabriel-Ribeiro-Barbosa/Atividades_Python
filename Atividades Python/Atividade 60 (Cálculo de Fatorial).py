#from math import factorial
#n = int(input('Insira um número: '))
#print('A fatorial de {} é {}'.format(n,factorial(n)))
n = int(input('Insira um número: '))
c = n
f = 1
print('A fatorial de {} é '.format(n))
print('{}! = '.format(n),end = '')
while c > 0 :
    print(c,end= '')
    print(' X 'if c >1 else ' = ',end= '')
    f *= c
    c -= 1
print(f)