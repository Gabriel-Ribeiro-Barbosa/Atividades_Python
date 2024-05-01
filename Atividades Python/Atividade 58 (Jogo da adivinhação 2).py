import random
print('Bem vindo ao jogo da adivinhação 2.0')
print('Eu vou pensar em um número de 0 á 10 e você tentara adivinhar')
jogar = input('Você quer jogar o jogo[S/N]: ').strip().upper()
lista = [0,1,2,3,4,5,6,7,8,9,10]
com = random.choice(lista)
cont = 0
while jogar  not in 'SN' :
    jogar = input('Eu te perguntei você quer jogar o jogo[S/N]: ').strip().upper()
if jogar == 'S' :
        print('Então vamos começar!!')
        num = int(input('Escolha seu palpite: '))
        while num not in lista :
            num = int(input('Você digitou errado,escolha seu palpite: '))
        while com != num  :
            cont += 1
            if com != num and com> num :
                num = int(input('É um número maior,escolha seu palpite: '))
            elif com != num and num> com :
                num = int(input('É um número menor,escolha seu palpite: '))
        if com == num :
            print('Parabéns você adivinhou!! No total foram {} tentativas'.format(cont+1))
else :
    print('Ok,volte quando quizer jogar...')