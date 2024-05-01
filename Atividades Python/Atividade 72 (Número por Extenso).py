cont = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True :
    n = int(input('Digite um número de 0 á 20: '))
    if n> 20 or n<0:
        print('\033[1;31mTente Novamente.',end= '')
    if 0 <= n <= 20 :
        print(f'\033[mVocê digitou o número {cont[n]}')
        add = input('Quer continuar?[S/N] ').strip().upper()
        if add not in 'SN' :
            add = input('\033[1;31mTente novamente,quer continuar?[S/N] \033[m').strip().upper()
        if add == 'N' :
            break