import requests
try:
    site = input('Insira o link do site: ')
    check = requests.get(site)
    print('Site está acessível.')
except:
    print(f'Site está indisponível.')
