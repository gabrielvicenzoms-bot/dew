tabu = int(input('insira o número que será feito a tabuada'))
vez = 1
resul = 0
while vez <11 and 0 < tabu < 11:
    resul = tabu * vez
    print(resul,'= ',tabu,'x', vez)
    vez = vez + 1
if tabu > 11 or tabu < 1:
    print('não é valido')
