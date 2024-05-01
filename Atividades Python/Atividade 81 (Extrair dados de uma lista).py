lista = []
cont = 0
while True :
    n = int(input('Digite um número: '))
    cont += 1
    lista.append(n)
    add = input('Quer continuar?[S/N]: ').strip().upper()
    while add not in 'SN' :
        add = input('Tente Novamente,quer continuar?[S/N]: ').strip().upper()
    if add == 'N' :
        break
lista.sort(reverse = True)
print(f'Foram digitados {cont} números')
print(f'Os valores em ordem decrescente: {lista}')
if 5 in lista :
    print(f'O número 5 está nas posiçoes: ',end = '')
    for v,c in enumerate(lista):
        if c == 5 :
            print(v,'...',end = '')
else :
    print('O número 5 não está na lista')