mulher20 = pessoa18 = homem = 0
while True :
    print('='*20)
    print('CADASTRE UMA PESSOA')
    idade = int(input('Idade: '))
    sexo = input('Sexo[M/F]: ').strip().upper()
    if sexo not in 'MF' :
        sexo = input('\033[1;31mInformação errada, digite seu sexo[M/F]:\033[m ').strip().upper()
    print('=' * 20)
    add = input('Quer continuar?[S/N] ').strip().upper()
    if add not in 'SN' :
        add = input('\033[1;31mTente Novamente,quer continuar?[S/N]\033[m ').strip().upper()
    if idade > 18 :
        pessoa18 += 1
    if sexo == 'M' :
        homem += 1
    if sexo == 'F' and idade < 20 :
        mulher20 += 1
    if add == 'N' :
        break
print(f'No total á {pessoa18} pessoas com mais de 18 anos\n{homem} homens foram cadastrados\nE temos {mulher20} mulheres com menos de 20 anos ')