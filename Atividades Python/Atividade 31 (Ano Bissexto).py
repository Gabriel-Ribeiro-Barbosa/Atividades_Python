import datetime
ano = int(input('Que ano deja analizar?(Digite 0 para o ano atual): '))
hoje = datetime.date.today().year
lista = [0]
if ano == 0 :
    ano = hoje
if ano % 4 == 0 and  ano % 100 != 0 or  ano & 400 == 0 :
     print('{} é um ano BISSEXTO!'.format(ano))
else:
    print('{} é NÃO é um ano BISSEXTO!'.format(ano))
