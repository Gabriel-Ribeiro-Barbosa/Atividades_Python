from time import sleep
def linha(esc):
    print('='*len(esc))
    print(esc)
    print('='*len(esc))
def contador(a,b,c):
    linha(f'Contagem de {a} até {b} de {c} em {c}: ')
    if a<b:
        for num in range(a,b+1,c):
            print(f'{num} ',end = '')#flush= True
            sleep(0.4)
        print()
    elif a>b:
        menos = c*(-1)
        for num in range(a,b,menos):
            print(f'{num} ', end='')
            sleep(0.4)
        if c %2 == 0:
            print(f'{b}',end= '')
        print()


contador(1,10,1)

contador(10,0,2)

inicio = int(input('Início da contagem: '))
fim = int(input('Fim da contagem: '))
passo = int(input('Quantos números serão pulados: '))
contador(inicio,fim,passo)