lista = []
pares = []
impar = []
while True :
    n = int(input('Digite um número: '))
    lista.append(n)
    add = input('Quer continuar?[S/N]: ').strip().upper()
    while add not in 'SN' :
        add = input('\033[1;31mTente Novamente ,quer continuar?[S/N]: \033[m').strip().upper()
    if add == 'N' :
        break
for c, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impar.append(v)
print(f'A lista completa é {lista}')
print(f'A lista par é {pares}')
print(f'A lista ímpar é {impar}')