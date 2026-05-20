numero1 = int(input('insira um número'))
numero2 = int(input('insira um outro número'))

if numero1 < numero2:
    numero1 = numero1 + 1
    for  number in range(numero1,numero2):
        print (number)

if numero1 > numero2:
    numero2 = numero2 + 1
    for  number in  range(numero2,numero1):
        print (number)
