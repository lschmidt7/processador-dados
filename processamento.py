
def localiza(dados, linha):
    quantidade_registros = len(dados)
    if linha < quantidade_registros:
        return dados[linha]
    else:
        print('Indice superior a quantidade de registros')
        return {}