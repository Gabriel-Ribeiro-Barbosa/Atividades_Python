s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1 :
    print('Esses segmentos FORMAM um triângulo',end= ' ')
    if s1 == s2 != s3 or s1 == s3 != s2  or s2 == s3 != s1:
        print('ISÓSCELES',end= ' ')
    elif s1 == s2 == s3 :
        print('EQUILÁTERO',end= ' ')
    elif s1 != s2 != s3 :
        print('ESCALENO',end= ' ')
else :
    print('Esses segmentos NÂO FORMAM um triângulo')


