salario = float(input('Qual o seu salário atual? R$ '))
if salario > 1250 :
    print('Você recebeu um aumento de 10% seu salário agora é R${}'.format(salario+(salario*10/100)))
else :
    print('Você recebeu um aumento de 15% seu salário agora é R${}'.format(salario+(salario*15/100)))
