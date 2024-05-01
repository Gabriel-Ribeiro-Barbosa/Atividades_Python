import datetime
ano = int(input('Ano do nscimento: '))
idade = datetime.date.today().year - ano
print('O atleta tem {} anos'.format(idade))
if idade <= 9 :
    print('Classificação: MIRIM')
elif idade <= 14 :
    print('Classificação: INFANTIL')
elif idade <= 19 :
    print('Classificação: JÚNIOR')
elif idade <= 25 :
    print('Classificação: SÊNIOR')
elif idade <= 60 :
    print('Classificação: MASTER')
elif idade > 60 :
    print('Classificação: \033[4;33m LENDA!!!')