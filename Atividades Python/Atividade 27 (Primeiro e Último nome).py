nome = input('Qual o seu nome: ').strip()
nomes = nome.split()
print('Seu primeiro nome é {}'.format(nomes[0]))
print('Seu último nome é {}'.format(nomes[len(nomes)-1]))