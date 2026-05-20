dados = 15
while dados > 0:
    nota = int(input('insira a nota'))
    if -1 < nota < 6:
        print(' a nota é', nota)
        dados = dados - 1
    else:
        print('nota invalída')
