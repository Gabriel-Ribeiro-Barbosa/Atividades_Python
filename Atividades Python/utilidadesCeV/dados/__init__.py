def leiadinheiro(n):
    valido=False
    while not valido:
        dado = str(input(n)).replace(',','.').strip()
        if dado.isalpha() or dado == '':
            print(f'\033[1;31mErro,\"{dado}\" não é um valor aceito\033[m')
        else:
            valido=True
            return float(dado)


