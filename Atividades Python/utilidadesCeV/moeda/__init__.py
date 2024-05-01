def metade(n,form=False):
    res = n/2
    return res if form == False else moeda(res)


def dobro(n,form=False):
    res = n*2
    return res if form == False else moeda(res)


def aumentar(n,por=0,form=False):
    res = n + (n*por/100)
    return res if form == False else moeda(res)


def reduzir(n,por=0,form=False):
    res = n - (n*por/100)
    return res if form == False else moeda(res)


def moeda(n):
    return f'R${n}'


def resumo(n,amt=10,rez=10):
    print('='*30)
    print('RESUMO DO VALOR'.center(30))
    print('=' * 30)
    print(f'Preço analizado: \t{moeda(n):>10}')
    print(f'Dobro do preço:  \t{dobro(n,True):>10}')
    print(f'Metade do preço: \t{metade(n,True):>10}')
    print(f'Com {amt}% de aumento: {aumentar(n,amt,True):>10}')
    print(f'COm {rez}% de redução: {reduzir(n,rez,True):>10} ')
    print('=' * 30)
