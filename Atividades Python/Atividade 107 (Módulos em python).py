import moeda
p = float(input('Digite um valor: R$'))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10% em {p} fica {moeda.aumentar(p,10)}')
print(f'Diminuindo 13% em {p} fica {moeda.reduzir(p,13)}')