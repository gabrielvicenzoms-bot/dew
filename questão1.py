i = int(input('informe a idade do estudante'))
ng = 0
np = i
while i >= 0:
    i = int(input('informe a idade do seu aluno'))
    if i > ng:
        ng = i
    
    if i < np and i > 0:
        np = i
if  np != i:
    print (ng)
    print (np)
    media = (np + ng) /2
    print (media)