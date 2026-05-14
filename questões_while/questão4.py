matricula = int(input('insira o número da mátricula do aluno'))
aprovado = 0
reprovado = 0
while 0 < matricula < 10000:
    nota1 = int(input('insira a primeira nota do aluno'))
    nota2 = int(input('insira a segunda  nota do aluno'))
    nota3 = int(input('insira a terceira nota do aluno'))
    media = (2*nota1 + 3*nota2 + 4*nota3) / 9

    print('a média final é', media)

    if media >= 5:
        aprovado = aprovado + 1
        print ('aprovado')
        
    if media < 5:
        reprovado = reprovado + 1
        print ('reprovado')
    
    
    matricula = int(input('insira o número da mátricula do aluno'))

total = aprovado + reprovado
print ('o total de alunos aprovados é', aprovado)
print ('o total de alunos reprovados é', reprovado)
    
print ('total de alunos é', total)
