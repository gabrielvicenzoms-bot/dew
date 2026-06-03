gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64,
3219.08]

junção = sum(gastos)

acima = 0
total= 0
for i in gastos:
    if i > 3000:
        acima += i
        total += 1


print(total)
print (junção)
porcentagem = (acima * 100) / junção

print (int(porcentagem))
