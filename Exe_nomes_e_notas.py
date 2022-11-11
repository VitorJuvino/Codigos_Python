

def nomes_notas():

    turma = []

    while True:

        nomes = input('Digite o nome do aluno, ou "FIM" para finalizar: ') 
        if nomes == 'fim':
            nomes = nomes.upper()
        if nomes == 'FIM':
            break
        turma.append(nomes)
        media_alunos = []

        for mediaAlunos in range(3):
            media = 0
            for nota in range(1, 4):
                n = float(input(f'Informe a {nota}º: '))
                media += n
            media_alunos.append(media // 3), 2
        turma.append(media_alunos)

    print(turma)

nomes_notas()

