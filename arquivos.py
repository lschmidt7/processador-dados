
def converte_dados(dado, tipo):
    dado_convertido = dado
    if tipo == int:
        dado_convertido = int(dado)
    elif tipo == float:
        dado_convertido = float(dado)
    elif tipo == bool:
        dado_convertido = False
        if dado == 'True':
            dado_convertido = True
    return dado_convertido

def carrega_arquivo(nome_arquivo, separador, tipos):

    f = open(nome_arquivo, 'r')
    linhas = f.readlines()

    cabecalho = linhas[0].replace('\n', '').split(separador)

    alunos = []

    # percorre as linhas do arquivo
    for linha in linhas[1:]:
        dados_linha = linha.replace('\n', '').split(separador)
        
        aluno = {}

        # percorre as colunas de cada linha
        for coluna, tipo in enumerate(tipos):

            campo = cabecalho[coluna]

            aluno[campo] = converte_dados(dados_linha[coluna], tipo)
        
        alunos.append(aluno)
    return alunos