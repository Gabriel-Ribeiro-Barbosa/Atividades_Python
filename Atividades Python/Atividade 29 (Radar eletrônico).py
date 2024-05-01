v = int(input('\033[1;40m Insira a velocidade atual do carro:\033[m '))
if v > 80 :
    print('\033[1;31m Você ultrapassou o limite permitido!!!\n Sua multa será de R${}'.format((v-80)*7))
else :
    print('\033[1;32m Você esta dentro do limite, continue assim!!')
print('\033[1;33m Tenha um bom dia.Dirija com segurança!')