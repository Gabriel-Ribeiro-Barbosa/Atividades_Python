matriz = []
somapar = soma3 = maior = 0
for l in range(0,3) :
    linha = []
    for c in range(0,3) :
        valor = int(input(f'Digite o termo [{l},{c}]: '))
        if valor % 2 == 0 :
            somapar += valor
        linha.append(valor)
    matriz.append(linha)
for l in range(0,3) :
    for c in range(0,3) :
        print(f'[{matriz[l][c]:^5}] ',end='')
    print()
for c in range(0,3) :
    soma3 += matriz[c][2]
for l in range(0,3) :
    if l == 1 :
        maior = matriz[1][l]
    if matriz[1][l] > maior :
        maior = matriz[1][l]
print(f'A soma dos valores pares de sua matriz é {somapar}')
print(f'A soma dos valores da 3 coluna é {soma3}')
print(f'O maior valor da 2 linha é {maior}')