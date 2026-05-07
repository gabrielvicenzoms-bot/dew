cod = int(input('informe o código do seu cargo'))
sal = int(input('informe o salario'))
soma = 0
qnt = 0


while 1 <= cod <= 3 :
   
    if cod == 3 and sal > 4500:
        qnt += 1
    cod = int(input('informe o código do seu cargo'))
    sal = int(input('informe o salario')) 


if qnt > 1:
    print ('a quantidade de médicos que ganham mais de 4500 é  ', qnt )


