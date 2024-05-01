#60R$ = 1dia  0.15R$ = 1km
km = float(input('Quantos km você andou? '))
dias = float(input('Quantos dias você ficou com o carro? '))
valor = (km*0.15) + (dias * 60)
print('Você gastou {}km em {} dias logo o valor a se pagar é de R${}'.format(km,dias,valor))