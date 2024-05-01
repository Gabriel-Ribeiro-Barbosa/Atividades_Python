from time import sleep
n = int(input('Informe um número para ser analisado: '))
print('Analisando')
print('.')
sleep(0.5)
print('.')
sleep(0.5)
print('.')
u = n//1%10
d = n//10%10
c = n//100%10
m = n//1000%10

print('Seu número possui : \n {} UNIDADE(S)\n {} DEZENA(S)\n {} CENTENA(S)\n {} MILHAR(ES)'.format(u,d,c,m))