n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversao:
[1] Converter BINÁRIO
[2] Converter OCTAL
[3] Converter HEXADECIMAL''')
opcao = int(input('Escolha uma das opções: '))
print('Sua opção: {}'.format(opcao))
if opcao == 1 :
    print('{} em BINÁRIO ficou: {}'.format(n, bin(n)[2:]))
elif opcao == 2 :
    print('{} em OCTAL ficou: {}'.format(n, oct(n)[2:]))
elif opcao ==3 :
    print('{} em HEXADECIMAL ficou: {}'.format(n, hex(n)[2:]))
else :
    print('\033[1;31mTente Novamente.Escolha um número ente 1 e 3')
