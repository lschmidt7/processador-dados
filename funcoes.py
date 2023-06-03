
def aplicar_funcao(dados, coluna, funcao):
    if funcao == 'media':
        return media(dados, coluna)
    if funcao == 'somatorio':
        return somatorio(dados, coluna)

def somatorio(dados, coluna):
    soma = 0
    for registro in dados:
        soma += registro[coluna]
    return soma

def media(dados, coluna):
    soma = 0
    for registro in dados:
        soma += registro[coluna]
    return soma / len(dados)