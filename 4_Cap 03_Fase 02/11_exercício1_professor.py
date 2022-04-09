#Resolução Professor

quantidade_alimentos = int(input("Informe quantos alimentos você consumiu hoje "))
total_caloria = 0

for alimento in range(1, quantidade_alimentos + 1, 1):
    caloria = int(input("Informe a caloria do alimento {} ". format(alimento)))
    total_caloria = total_caloria + caloria

print("Você consumiu {} calorias ao total no dia." .format(total_caloria))