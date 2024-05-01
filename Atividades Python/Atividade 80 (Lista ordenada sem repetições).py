lista = []
for v in range(0,5) :
    n = int(input('Digite um número: '))
    if v == 0 or n> lista[-1] :
        lista.append(n)
        print('Foi adicionado no final da lista...')
    else :
        posicao = 0
        while posicao < len(lista) :
            if n <= lista[posicao] :
                lista.insert(posicao,n)
                print(f'Foi adicionado na posição {posicao} da lista...')
                break
            posicao += 1
print('-_-'*20)
print(f'Sua lista ficou assim: {lista}')