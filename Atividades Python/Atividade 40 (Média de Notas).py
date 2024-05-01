n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
med = (n1 + n2)/2
print('As notas do aluno foram {} e {} logo a média é {}'.format(n1,n2,med))
if med >= 7 :
    print('\033[1;32mAluno  APROVADO!')
elif  5 <= med <= 6.9 :
    print('\033[1;33mAluno está de RECUPERÇÃO!')
else :
    print('\033[1;31mAluno REPROVADO!')

