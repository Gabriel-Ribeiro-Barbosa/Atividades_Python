sexo = str(input('Qual o seu sexo[M/F] : ')).strip().upper()
while sexo not in 'MF':
    sexo = str(input('Dado invalido, por favor insira seu sexo[M/F] : ')).strip().upper()
print('Dado valido,seu sexo é {}'.format(sexo))


