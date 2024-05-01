import moeda
p = float(input('Digite um valor: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p,True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p,True)}')
print(f'Aumentando 10% em {moeda.moeda(p)} fica {moeda.aumentar(p,10,True)}')
print(f'Diminuindo 13% em {moeda.moeda(p)} fica {moeda.reduzir(p,13,True)}')