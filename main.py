from arquivos import carrega_arquivo
from processamento import localiza

alunos = carrega_arquivo('dados/alunos.csv', ',', [str, int, str, float, float, int, float, bool])

linha = localiza(alunos, 4999)

print(linha)