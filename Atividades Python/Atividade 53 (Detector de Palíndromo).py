frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()#separar
junto = ''.join(palavra)#junta em um str só
inverso = ''
for c in range(len(junto) -1,-1,-1) :
    inverso = inverso + junto[c]
print('{} ao contrário fica {}'.format(frase,inverso))
if inverso == junto :
    print('A frase digitada é um PALÍNDROMO!')
else:
    print('A frae digitada NÃO é um palíndromo!')