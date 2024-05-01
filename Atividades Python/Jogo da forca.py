from Forca import *
from Forca.Arquivo import *
from Forca.Palavras import *

face('FORCA THE GAME')
palavra = gerar(lista)
certa = []
errada = []
tentativas = 5
color(f'Vamos começar, tente adivinha a palavra: ',5)
while True:
    for letra in palavra:
        if letra in certa:
            print(letra,end = '')
        else:
            print('_ ',end = '')
    escolha = input('\nEscolha uma letra: ').strip().lower()
    if escolha in palavra:
        certa.append(escolha)
        color(f'Letras certar: {certa}',2)
    else:
        errada.append(escolha)
        color(f'Letras erradas: {errada}',1)
        tentativas -= 1
    print(f'Você tem {tentativas} tentativas')
    if tentativas == 0:
         color('Você perdeu tente outra vez!!',1)
         break
    vitoria = True
    for letra in palavra:
        if letra.lower() not in certa:
            vitoria = False
    if vitoria:
        color('FIM DE JOGO USUÁRIO VENCEU!!!',2)
        color(f'Você ficou com {tentativas} tentativas e errou {len(errada)} vezes',5)
        break