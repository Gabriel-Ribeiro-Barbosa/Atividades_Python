from menu.principal import *
from menu.arquivo import *
from time import sleep
a = 'Arquivo de Dados.txt'
if a_existe(a):
    print('Arquivo foi encontrado com sucesso!!')
else:
    print(color('Arquivo não foi encontrado',1))
    a_nexiste(a)
while True:
    l('MENU DE OPÇÕES',c=True)
    opcao = dado(color('Qual sua opção: ',3))
    if opcao not in (1,2,3):
        print(color('Erro,digite uma opção valida', 1))
    else:
        if opcao == 1:
           lera(a)
        elif opcao == 2:
            l('NOVO CADASTRO',False)
            nome = input('Digite seu nome: ')
            idade = leiaInt('Digite sua idade: ')
            cadastro(a,nome,idade)
        elif opcao == 3:
            print(color('Finalizando o programa',4),end= '')
            tempo()
            print(color('Programa finalizado,volte sempre!!!',4))
            break
    sleep(2)







