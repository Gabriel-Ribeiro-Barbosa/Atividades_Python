times = ('Palmeiras','Grêmio','Atlético MG','Flamengo','Botafogo','Bragantino',
         'Fluminense','Atlético PR','Internacional','Fortaleza','São Paulo',
         'Cuiaba','Corinthians','Cruzeiro','Vasco','Bahia','Santos','Goiás',
         'Coritiba','Juventude')
print(f'Times do Brasileirão 2023 = {times}')
print('='*60)
print(f'Os 5 primeiros são: {times[0:5]}')
print('='*60)
print(f'Os 4 últimos são : {times[16:21]}')
print('='*60)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('='*60)
print(f'O Internacional está na {times.index('Internacional')+1}° posição')
print('='*60)