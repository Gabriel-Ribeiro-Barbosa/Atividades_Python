print('\033[1;33m=-='*5,end= ' ')
print('\033[1;32mLOJA DO JÃO',end= ' ')
print('\033[1;33m=-='*5,end = ' ')
preco = float(input('\n\033[mInsira o valor a ser pago pelo produto: R$'))
print('''FORMAS DE PAGAMENTO:
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no catão
[4] 3x ou mais no cartão''')
opcao = int(input('Qual é a sua opção: '))
if opcao in (1,2,3,4) :
    if opcao == 1 :
        print('Você optou por pagar a vista, ganhando assim um desconto de 10%')
        print('Sua compra de R${} ficou R${}'.format(preco,preco - (preco*10/1000)))
    elif opcao == 2 :
        print('Você optou po pagar a vista no catão, ganhando assim um desconto de 5%')
        print('Sua compra de R${} ficou R${}'.format(preco,preco - (preco*5/100)))
    elif opcao == 3 :
        print('Você optou por pagar em 2x no cartão')
        print('Sua compra de R${}, ficou no total de duas parcelas de R${}'.format(preco,preco/2))
    elif opcao == 4 :
        parcela = int(input('Em quantas parcelas deseja pagar:  '))
        print('Você optou por pagar em {}x no cartão, possuindo assim um juros de 20%'.format(parcela))
        print('Sua compra de R${} vai dar no total R${}, cada parcela ficara R${}'.format(preco,preco + (preco*20/100),(preco + (preco*20/100)) / parcela))
    print('\033[1;36mMuito obrigado, volte sempre!!')
else :
    print('\033[1;31mTente Novamente, digite um número de 1 á 4')