jogador = dict()
lista = []
soma = 0
jogador['nome'] = input('Nome do jogador: ')
jogador['partidas'] = int(input('Partidas jogadas: '))
for c in range(1,jogador['partidas']+1) :
    gol = int(input(f'Quantos gols fez na {c}° partida: '))
    lista.append(gol)
    soma += gol
jogador['gols'] = lista
jogador['total'] = soma
print('=-'*30)
print(jogador)
print('=-'*30)
for k,v in jogador.items() :
    print(f'O campo {k} tem valor {v}')
print('=-'*30)
print(f'O jogador {jogador['nome']} jogou {jogador['partidas']} partidas')
for p,g in enumerate(lista):
    print(f'    -> Na partida {p+1} fez {g} gols')
print(f'No total {jogador['nome']} fez {soma} gols')
print('=-'*30)