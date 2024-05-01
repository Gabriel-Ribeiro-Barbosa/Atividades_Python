lista = []
while True :
    numeros = int(input('Digite um número: '))
    if numeros not in lista :
        lista.append(numeros)
    else :
        print('Não irei adicionar, valor duplicado!!')
    add = input('Quer continuar?[S/N]: ').strip().upper()
    while add not in 'SN' :
        add = input('Tente Novamente,quer continuar?[S/N]: ').strip().upper()
    if add == 'N' :
        break
print('=-='*15)
print(f'Sua lista ficou assim: {sorted(lista)}')