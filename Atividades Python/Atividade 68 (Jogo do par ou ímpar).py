import random
cont = 0
while True :
    lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    com = random.choice(lista)
    comecar = input('\033[mQuer jogar par ou ímpar comigo?[S/N] ').strip().upper()
    if comecar not in 'SN':
        comecar = input('\033[1;31mEu te perguntei, você quer Jogar par ou ímpar comigo?[S/N]\033[m ').strip().upper()
    if comecar == 'N' :
        print('Volte quando quizer jogar...')
        break
    elif comecar == 'S' :
        n = int(input('Escolha um número de 0 á 10: '))
        if n > 10:
            n = int(input('\033[1;31mEscolha incorreta, indique um número de 0 á 10: \033[m'))
        escolha = input('Par ou ímpar[P/I]: ').strip().upper()
        if escolha not in 'PI':
            escolha = input('\033[1;31mEscolha uma das opções, par ou ímpar[P/I]: \033[m').strip().upper()
        soma = com + n
        if soma % 2 == 0 :
            print(f'Você jogou {n} e computador jogou {com} o total deu {soma}.Logo deu PAR')
        else :
            print(f'Você jogou {n} e computador jogou {com} o total deu {soma}.Logo deu ÍMPAR')
        if escolha == 'P':
            if soma % 2 == 0:
                cont += 1
                print('\033[1;32mJogador venceu!!')
                print('Vamos jogar novamente...')
            elif soma % 2 != 0 :
                print('\033[1;33mComputador venceu!!')
                print('O jogo acabou')
                break
        elif escolha == 'I' :
            if soma % 2 != 0:
                cont += 1
                print('\033[1;32mJogador venceu!!')
                print('Vamos jogar novamente...')
            elif soma % 2 == 0 :
                print('\033[1;33mComputador venceu!!')
                print('O jogo acabou')
                break
print(f'\033[1;34mVocê venceu {cont} vezes consecutivas')