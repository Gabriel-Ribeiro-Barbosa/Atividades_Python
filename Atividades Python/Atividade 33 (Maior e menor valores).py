n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
maior = n1
if n2>n3 and n2>n1 :
    maior = n2
if n3 > n2 and n3 > n1 :
    maior = n3
menor = n1
if n2< n1 and n2 < n3 :
    menor = n2
if n3 < n1 and n3 < n2 :
    menor = n3
print('O maior é {} e o menor é {}'.format(maior,menor))
#if n1 > n2 and n1 > n3 :
    #print('\033[1;32m O MAIOR número é {}'.format(n1))
#elif n2 > n1 and n2 > n3 :
    #print('\033[1;32mO MAIOR número é {}'.format(n2))
#else :
    #print('\033[1;32mO MAIOR número é {}'.format(n3))
#if n1 < n2 and n1 < n3 :
    #print('\033[1;31mO MENOR número é {}'.format(n1))
#elif n2 < n1 and n2 < n3 :
    #print('\033[1;31mO MENOR número é {}'.format(n2))
#else :
    #print('\033[1;31mO MENOR número é {}'.format(n3))