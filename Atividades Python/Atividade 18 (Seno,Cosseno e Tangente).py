import math
angulo = float(input('Digite o ângulo a ser analisado: '))
print('O ângulo {} tem o SENO de {:.2}\n O COSSENO de {:.2}\n E a TANGENTE de {:.2}'.format(angulo,math.sin(math.radians(angulo)),math.cos(math.radians(angulo)),math.tan(math.radians(angulo))))