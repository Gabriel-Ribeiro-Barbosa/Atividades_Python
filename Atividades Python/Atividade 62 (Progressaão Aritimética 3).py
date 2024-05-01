p1 = int(input('Qual o seu primeiro termo: '))
r = int(input('Qual a razão: '))
termo = p1
cont = 1
add = 10
tot = 0
print('{} -> '.format(p1),end='')
while add != 0 :
    tot += add
    while cont <=tot:
        print('{} -> '.format(termo),end='')
        termo += r
        cont += 1
    print('PAUSA',end='')
    add = int(input('\nQuantos termos a mais você deseja adicionar: '))
print('Finalizando P.A , no total foram {} termos '.format(tot))