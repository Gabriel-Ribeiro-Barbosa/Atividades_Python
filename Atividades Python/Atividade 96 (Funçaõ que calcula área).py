def linha():
    print('='*20)
def area(a,b):
    area = a*b
    print(f'A área de um terreno {a}m X {b}m é igual a {area:.2f}m²')


linha()
print('Controle de Terrenos'.center(20))
linha()
largura = float(input('Qual a largura: '))
altura = float(input('Qual a altura: '))
area(largura,altura)