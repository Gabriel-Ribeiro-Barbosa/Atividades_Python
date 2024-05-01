import datetime
ano = int(input('Qual seu ano de nascimento: '))
idade = datetime.date.today().year - ano
print('Você nasceu em {} então possui {} ano(s)'.format(ano,idade))
if idade < 18 :
    print('Ainda faltam {} anos para o seu alistamento'.format(18-idade))
    print('Seu alistamento será em {}'.format(datetime.date.today().year +(18-idade)))
elif idade == 18 :
    print('Seu alistamento é esse nao, ALISTE-SE JÁ!!')
else :
    print('Seu alistamento ja deveria ter ocorrido faz {} anos'.format(idade - 18))
    print('Seu alistamento ocorreu em {}'.format(datetime.date.today().year - (idade - 18)))


