temp = int(input('informe a temperatura'))
quantidade = 0
total = 0
while  temp != -273:
    quantidade  = quantidade + 1
    total = (total + temp) 
    temp = int(input('informe a temperatura'))
    

divisao = total/quantidade
print (divisao)