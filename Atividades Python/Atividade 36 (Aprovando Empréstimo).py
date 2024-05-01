print('Bem vindo, analizarei se você pode efetuar o empréstimo')
print('Responda as perguntas a seguir: ')
casa = float(input('Valor da casa: '))
salario = float(input('Seu salário: '))
anos = int(input('Anos que pretende pagar: '))
prestacao = casa / (anos * 12)
print('Você recebe R${} e pretende comprar uma casa de R${} em {} anos sua prestação sera de R${:.2f}'.format(salario,casa,anos,prestacao))
if prestacao <= (salario*30/100) :
    print('\033[1;32mPrestacão APROVADA!!')
else :
    print('\033[1;31mPrestação RECUSADA!!')