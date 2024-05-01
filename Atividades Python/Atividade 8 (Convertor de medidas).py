m = float(input('Qual o seu valor em metros: '))
km = (m/1000)
hm = (m/100)
dam = (m/10)
dm = (m*10)
cm = (m*100)
mm = (m*1000)

print('{}m equivale a: \n {} km \n {} hm\n {} dam\n {} dm\n {} cm\n {} mm '.format(m,km,hm,dam,dm,cm,mm))