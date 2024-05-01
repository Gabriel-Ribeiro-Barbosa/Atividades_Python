#1lata = 2m
largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
area = largura*altura
tinta = area/2
print('A largura da sua parede é {}m e a altura é {}m logo sua área é de {:.2f}m2'.format(largura,altura,area))
print('Sera nescessário {:.2f} latas de tinta'.format(tinta))