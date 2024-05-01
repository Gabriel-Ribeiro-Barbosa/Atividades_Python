s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 + s2 > s3 and  s1 + s3 > s2 and s2 + s3 > s1 :
    print("\033[1;32m Esses segmentos formam um triângulo")
else :
    print('\033[1;31m Esses segmentos não formam um triângulo')