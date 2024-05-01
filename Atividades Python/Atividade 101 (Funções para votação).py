def voto(v):
    idade = 2024-v
    if 65 >= idade >= 18:
        return f'Com {idade} anos seu voto é OBRIGATÓRIO!!!'
    elif idade > 65 or 17 <= idade >= 16:
        return f'Com {idade} anos seu voto é OPICIONAL'
    else:
        return f'Com {idade} anos você não pode votar!!'


ano = int(input('Qual o ano do seu nascimento: '))
print(voto(ano))
