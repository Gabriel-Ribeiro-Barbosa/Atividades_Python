princ = []
lista = []
maior = menor = 0
menorn = maiorn = ''
while True :
    lista.append(input('Qual é seu nome? ').strip())
    lista.append(float(input('Qual é o seu peso: Kg')))
    if len(princ) == 0:
        maior = lista[1]
        menor = lista[1]
    else :
        if lista[1] > maior :
            maior = lista[1]
        if lista[1] < menor :
            menor = lista[1]
    princ.append(lista[:])
    lista.clear()
    add = input('Quer continuar[S/N]? ').strip().upper()
    while add not in 'SN' :
        add = input('\033[1;31mTente Novamente,quer continuar[S/N]? \033[m').strip().upper()
    if add == 'N' :
        break
print('=-'*30)
print(f'Ao todo você cadastrou {len(princ)} pessoas')
print(f'O maior peso foi Kg{maior} de: ',end= '')
for p in princ :
    if p[1] == maior:
        print(f'[{p[0]}]',end= '')
print(f'\nO menor peso foi Kg{menor} de: ',end= '')
for p in princ :
    if p[1] == menor :
        print(f'[{p[0]}]')
print('=-'*30)