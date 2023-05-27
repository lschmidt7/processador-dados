from arquivos import carrega_arquivo
from processamento import localiza, filtrar, projetar

alunos = carrega_arquivo('dados/alunos.csv', ',', [str, int, str, float, float, int, float, bool])

# linha = localiza(alunos, 4999)

alunos_pedro_ii = filtrar(alunos, 'escola', 'Pedro II', '==')

print(len(alunos_pedro_ii))

alunos_pedro_ii_monitoria = filtrar(alunos_pedro_ii, 'monitoria', True, '==')

print(len(alunos_pedro_ii_monitoria))

alunos_pedro_ii_monitoria_sem1_7 = filtrar(alunos_pedro_ii_monitoria, 'nota_semestre_1', 7, '>')

print(len(alunos_pedro_ii_monitoria_sem1_7))

alunos_pedro_ii_monitoria_sem1_7_projetado = projetar(alunos_pedro_ii_monitoria_sem1_7, ['nome', 'nota_semestre_1', 'monitoria'])

aluno = localiza(alunos_pedro_ii_monitoria_sem1_7_projetado, 0)

print(aluno)