add = 'S'
cont = media = soma = maior = menor = 0
while add == 'S' :
    num = int(input('\033[1;32mDigite um número: '))
    cont += 1
    soma += num
    add = input('\033[1;33mQuer continuar[S/N]: ').strip().upper()
    while add not in 'SN':
        add = input('\033[1;31mErro na sua resposta,você quer continuar[S/N]: ').strip().upper()
    if cont == 1 :
        maior = num
        menor = num
    elif num > maior :
        maior = num
    elif num< menor:
        menor = num
    media = soma / cont
else:
    print('\033[1;34mVocê digitou {} números e a média foi {:.2f}'.format(cont,media))
    print('O maior é o {} e o menor é o {}'.format(maior,menor))