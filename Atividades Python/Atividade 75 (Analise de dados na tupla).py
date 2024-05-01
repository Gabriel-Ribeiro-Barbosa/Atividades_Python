num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um  número: ')),
       int(input('Digite um último número: ')))
if 9 in num :
    print(f'O valor 9 apareceu {num.count(9)} vezes')
else :
    print('Não ouve número 9')
if 3 in num :
    print(f'O valor 3 apareceu na {num.index(3) +1}° posicão')
else :
    print('Não ouve número 3')
print(f'Os valores pares foram no total: ',end='')
for n in num :
    if n % 2 == 0:
        print(n ,' ',end='')