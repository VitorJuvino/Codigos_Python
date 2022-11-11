
# Atividade do beecrowd

n1, n2, n3, n4 = input().split()

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = (n1*2 + n2*3 + n3*4 + n4*1) / 10

if media >= 7.0:
    print(f'Media: {media:.1f}')
    print(f'Aluno aprovado.')

if media < 5.0:
    print(f'Media: {media:.1f}')
    print(f'Aluno reprovado.')

if 5.0 <= media <= 6.9:
    
    print(f'Media: {media:.1f}')
    print(f'Aluno em exame.')
    exame = float(input())
    nota = (exame + media) / 2
    print(f'Nota do exame: {exame:.1f}')
    
    if nota >= 5.0:
        print(f'Aluno aprovado.')
        print(f'Media final: {nota:.1f}')
    else:
        print(f'Aluno reprovado.')
        print(f'Media final: {nota:.1f}')

        

