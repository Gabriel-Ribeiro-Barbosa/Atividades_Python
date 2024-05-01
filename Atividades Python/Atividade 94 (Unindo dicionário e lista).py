cadastro = dict()
lista = list()
cont = soma = 0
while True:
    print('-='*10)
    print(f'     {cont+1}° PESSOA'.center(10))
    print('-='*10)
    cont+= 1
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    soma+= idade
    media = idade/cont
    sexo = ''
    while sexo == '' or sexo not in 'MF':
        sexo = input('\033[mDigite o seu sexo[M/F]: ').strip().upper()
        if sexo not in 'MF' :
            print('\033[1;31mErro! por favor digite [M/F]: ')
    cadastro['nome'] = nome
    cadastro['sexo'] = sexo
    cadastro['idade'] = idade
    lista.append(cadastro.copy())
    add = ''
    while add == '' or add not in 'NS':
        add = input('\033[mQuer continuar?[S/N]: ').strip().upper()
        if add not in 'NS':
            print('\033[1;31mErro! por favor digite [S/N]: ')
    if add == 'N':
        break
print('=-'*20)
print(f'A) Ao todo foram cadastradas {len(lista)} pessoas')
print(f'B) A média de idade do grupo é {media:5.2f}')
print(f'C) As mulheres cadastradas foram ',end = '')
for v in lista:
    if v['sexo'] == 'F':
        print(f'{v['nome']}; ',end= '')
print(f'\nD) Lista de pessoas que estão acima da média: ')
print('   ')
for v in lista:
    if v['idade'] >= media:
        for k,t in v.items():
            print(f'{k} = {t}; ',end= '')
        print()
print('=-'*20)
print('FIM')