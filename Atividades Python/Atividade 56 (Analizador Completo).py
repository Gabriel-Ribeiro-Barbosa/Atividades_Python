homemmaisvelho = 0
mulher20 = 0
soma = 0
nomemaisvelho = ''
media = 0
for c in range (1,5) :
    print('='*20)
    print('     {}° PESSOA'.format(c))
    print('=' * 20)
    idade = int(input('Sua idade: '))
    sexo = str(input('Seu sexo(M/F): ')).strip().upper()
    nome = str(input('Seu nome: ')).strip()
    soma += idade
    if c == 1 and sexo == 'M':
        homemmaisvelho = idade
        nomemaisvelho = nome
    if sexo =='M' and idade > homemmaisvelho :
        homemmaisvelho = idade
        nomemaisvelho = nome
    if sexo == 'F' and idade <20 :
         mulher20 += 1
    media = soma/4
print('A média de idade do grupo é {}'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(homemmaisvelho,nomemaisvelho))
print('No total á {} mulheres com menos de 20 anos'.format(mulher20))