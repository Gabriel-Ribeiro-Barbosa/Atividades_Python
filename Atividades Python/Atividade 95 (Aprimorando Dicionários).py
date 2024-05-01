from time import sleep
cont = 0
jogador = dict()
lista = list()
tabela = list()
while True:
    soma = 0
    jogador.clear()
    lista.clear()
    print('='*20)
    print(f'JOGADOR {cont+1}'.center(20))
    print('='*20)
    cont+= 1
    nome = input('Nome do jogador: ')
    partidas = int(input(f'Quantas partidas {nome} jogou? '))
    jogador['NOME'] = nome
    jogador['PARTIDAS'] = partidas
    for g in range(0,partidas):
        gols= int(input(f'Quantos gols fez na {g+1}° partida: '))
        soma += gols
        lista.append(gols)
    jogador['GOLS'] = lista[:]
    jogador['TOTAL'] = soma
    tabela.append(jogador.copy())
    while True :
        add = input('\033[mQuer continuar?[S/N]: ').strip().upper()
        if add  in 'SN':
            break
        else:
             print('\033[1;31mErro, por favor digite [S/N]: ')
    if add == 'N':
        break
print('=-='*20)
print(f'{'N°':<4}',end = '')
for k in jogador.keys():
    print(f'{k:<15}',end = '')
print()
print('=-='*20)
for c,v in enumerate(tabela):
    print(f'{c:<3} ',end = '')
    for t in v.values():
        print(f'{str(t):<15}',end = '')
    print()
print('=-='*20)
while True:
    termo = int(input('\033[mQual jogador quer ver?[999 para parar]: '))
    if termo == 999:
        break
    if termo >= len(tabela):
        print('\033[1;31mErrro por favor digite um número correspondente: ')
    else:
        for c,v in enumerate(tabela[termo]['GOLS']) :
            print(f'Na partida {c} fez {v} gols')
    print('=-='*20)
print('Finalizando programa',end = '')
for c in range(0,3) :
    print('.',end = '')
    sleep(0.5)
print()
print('Programa finalizado!!!')