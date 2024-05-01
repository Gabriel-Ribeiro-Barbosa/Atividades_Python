peso = float(input('Insira seu peso: (Kg)'))
altura = float(input('Insira sua altura: (m)'))
imc = peso / (altura**2)
print('O seu IMC é {:.2f}'.format(imc))
if imc < 18.5 :
    print('Você está ABAIXO DO PESO')
elif imc < 25 :
    print('Você está com o PESO IDEAL')
elif imc < 30 :
    print('Você está com SOBREPESO')
elif imc < 40 :
    print('Você está com OBESIDADE')
elif imc > 40 :
    print('Você está com OBESIDADE MORBIDA!!!')