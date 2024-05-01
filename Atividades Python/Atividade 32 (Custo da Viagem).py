dis = float(input('Informe a distância de sua viagem: '))
if dis >200 :
    print('Sua viagem vai custar R${}'.format(dis*0.45))
else:
    print('SUa viagem vai custar R${}'.format(dis*0.50))