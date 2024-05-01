salario = float(input('Qual o salário do funcionário? R$'))
aumento = salario * (15/100)
print('O funcionario a seguir teve um aumento de 15% em seu salário logo passara de R${} para R${:.2f}'.format(salario,aumento+ salario))