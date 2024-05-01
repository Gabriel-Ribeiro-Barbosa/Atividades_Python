num = [[],[]]
principal = []
for c in range(1,8) :
    valor = int(input(f'Digite o {c}° valor: '))
    if valor % 2 == 0 :
        num[0].append(valor)
    else :
        num[1].append(valor)
print(f'Sua lista par ficou: {sorted(num[0])}')
print(f'Sua lista ímpar ficou: {sorted(num[1])}')