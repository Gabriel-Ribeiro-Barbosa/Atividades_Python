valor = float(input('Qual o preço do produto? R$'))
desconto = valor *(5/100)
print('Você obteve um desconto de 5% logo o valor a se pagar é de R${:.2f}'.format(valor- desconto))