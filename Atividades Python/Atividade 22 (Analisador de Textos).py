nome = input('Digite o seu nome: ').strip()
print('Seu nome em maiúsculo fica {} '.format(nome.upper()))
print('Seu nome em minúsculo fica {}'.format(nome.lower()))
print('Seu nome possui {} letras'.format(len(nome)- nome.count(' ')))
separar = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separar[0],len(separar[0])))

