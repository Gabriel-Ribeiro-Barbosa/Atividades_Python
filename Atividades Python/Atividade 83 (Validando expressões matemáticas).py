expr = input('Digite uma expreção: ')
lista = []
for simbolo in expr :
    if simbolo == '(' :
        lista.append('(')
    elif simbolo == ')':
        if len(lista) > 0 :
            lista.pop()
        else :
            lista.append(')')
            break
if len(lista) == 0 :
    print('A expressão é valida!')
else :
    print('A expressão não é valida!!')