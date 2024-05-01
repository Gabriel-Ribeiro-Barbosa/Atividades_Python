def ficha(n):
    if n == '':
        return '<desconhecido>'

    else:
        return n

nome = str(input('Nome do jogador: ')).strip()
gols = str(input('Gols na carreira: ')).strip()
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
print(f'Jogador {ficha(nome)} fez {ficha(gols)} gols na carreira')