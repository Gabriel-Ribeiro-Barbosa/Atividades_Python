soma = mil = precobarato = cont = 0
nomebarato = ''
print('=-'*15)
print('      LOJA DO SEU JUCA')
print('=-'*15)
while True :
    produto = input('Nome do produto comprado: ').strip()
    preco = float(input('Preço do produto: R$'))
    cont += 1
    soma += preco
    add = input('Quer continuar?[S/N] ').strip().upper()
    if preco > 1000 :
        mil += 1
    if cont == 1 :
        precobarato = preco
        nomebarato = produto
    else:
        if preco < precobarato :
            precobarato = preco
            nomebarato = produto
    if add not in 'SN' :
        add = input('\033[1;31mTente Novamente,quer continuar?[S/N]\033[m ').strip().upper()
    if add == 'N' :
        break
print(f'O total das compras deu R${soma}\nTemos {mil} produtos com o preço maior do que R$1000\nO produto mais barato é a(o) {nomebarato} e custa R${precobarato}')