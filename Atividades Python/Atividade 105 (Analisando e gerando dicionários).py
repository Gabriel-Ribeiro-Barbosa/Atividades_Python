def notas(*num,sit=False):
    """
-> Ler notas e transformar em dicionário
    :param num: As notas que serão transformadas
    :param sit: Um parametro opicional que gere ou não a situação
    :return: Retorna o dicionário com o histórico do aluno
    """
    res = dict()
    soma = sum(num)
    med = soma/(len(num))
    res['total'] = len(num)
    res['maior'] = max(num)
    res['menor'] = min(num)
    res['média'] = med
    if sit:
        if res['média'] >= 7:
            res['situação'] = 'BOA'
        elif res['média'] >= 5:
            res['situação'] = 'RAZOÁVEL'
        else:
            res['situação'] = 'RUIM'
    return res


res = notas(4,9,7,10,9.5,sit=True)
print(res)
help(notas)