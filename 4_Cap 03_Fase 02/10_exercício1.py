quantidade_alimentos = int(input("Informe quantos alimentos você consumiu hoje "))
alimento = 0
total_caloria = 0

for x in range(quantidade_alimentos):
    alimento += 1
    caloria = int(input("Informe a caloria do alimento {} ". format(alimento)))
    total_caloria = total_caloria + caloria

print(total_caloria)


