valores = []
for v in range (0,5):
    valores.append(int(input(f'Digite o número da posição {v}: ')))
maior = max(valores)
menor = min(valores)
print(f'Você digitou os seguintes valores: {valores}')
print(f'O maior valor foi {maior} nas posições: ',end='')
for i,v in enumerate(valores) :
    if v == maior :
        print(f'{i}... ',end='')
print(f'\nO menor valor foi {menor} nas posições: ',end='')
for i,v in enumerate(valores) :
    if v == menor :
        print(f'{i}... ',end='')