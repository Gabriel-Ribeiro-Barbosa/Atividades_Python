print('='*30)
print('     10 TERMOS DE UMA PA     ')
print('='*30,)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + (10-1) * razao
for c in range (primeiro,decimo + 1,razao) :
    print(c,'->',end= ' ')
print('FIM',end= ' ')