totmaior = 0
totmenor = 0
for c in range (1,8) :
    ano = int(input('Em que ano a {}° pessoa nasceu: '.format(c)))
    idade = (2024 - ano)
    if idade >= 21 :
        totmaior += 1
    else:
        totmenor += 1
print('No total {} pessoas atingiram a maioridade'.format(totmaior))
print('No total {} pessoas não atingiram a maioridade'.format(totmenor))
