usuario = dict()
usuario['nome'] = input('Nome: ')
usuario['ano'] = int(input('Ano de nascimento: '))
usuario['trabalho'] = int(input('Número da carteira de trabalho[0 para nulo]: '))
if usuario['trabalho'] != 0 :
    usuario['contratacao'] = int(input('Ano de contratação: '))
    usuario['salario'] = float(input('Salário: R$'))
print('=-'*20)
print(f'''O nome é {usuario['nome'] }
A idade é {2024 - usuario['ano']}
A carteira tem o número {usuario['trabalho']}''')
if usuario['trabalho'] != 0 :
    print(f'''O salário é de R${usuario['salario']}'
A aposentadoria ocorrera quando você tiver {2024 - usuario['contratacao'] + 35 }''')
print('=-'*20)