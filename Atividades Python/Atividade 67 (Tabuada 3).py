t = c = 0
while True :
    print('='*43)
    t = int(input('Insira um número para calcular sua tabuada: '))
    print('='*43)
    if t <0 :
        break
    for c in range (1,11):
        print(f'''{t} X {c} = {t*c}''')
print('TABUADA incerrada ,volte sempre!!')