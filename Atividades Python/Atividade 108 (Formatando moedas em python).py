import moeda
p = float(input('Digite um valor: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10% em {moeda.moeda(p)} fica {moeda.moeda(moeda.aumentar(p,10))}')
print(f'Diminuindo 13% em {moeda.moeda(p)} fica {moeda.moeda(moeda.reduzir(p,13))}')