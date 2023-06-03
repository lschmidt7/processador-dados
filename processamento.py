from funcoes import aplicar_funcao

def localiza(dados, linha):
    quantidade_registros = len(dados)
    if linha < quantidade_registros:
        return dados[linha]
    else:
        print('Indice superior a quantidade de registros')
        return {}

def testar(v1, operacao, v2):
    if operacao == '==':
        return v1 == v2
    elif operacao == '>':
        return v1 > v2
    elif operacao == '<':
        return v1 < v2
    elif operacao == '>=':
        return v1 >= v2
    elif operacao == '<=':
        return v1 <= v2
    elif operacao == '!=':
        return v1 != v2
    return False

def filtrar(dados, coluna, valor, operacao):
    dados_filtrados = []
    for linha in dados:
        if testar(linha[coluna], operacao, valor):
            dados_filtrados.append(linha)
    return dados_filtrados

def projetar(dados, colunas):
    dados_projetados = []
    for linha in dados:
        linha_projetada = {}
        for campo, valor in linha.items():
            if campo in colunas:
                linha_projetada[campo] = valor
        dados_projetados.append(linha_projetada)
    return dados_projetados

def agrupar(dados, coluna, coluna2, funcao):

    dados_agrupados = {}

    for linha in dados:
        valor_celula = linha[coluna]
        if dados_agrupados.get(valor_celula) == None:
            dados_agrupados[valor_celula] = []
        dados_agrupados[valor_celula].append(linha)
    
    for chave, lista in dados_agrupados.items():
        dados_agrupados[chave] = aplicar_funcao(lista, coluna2, funcao)
    
    return dados_agrupados