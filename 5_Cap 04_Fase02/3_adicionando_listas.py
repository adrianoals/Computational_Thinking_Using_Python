
jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]

#incluindo um valor no final da lista
jedi.append("Mace Windu")

for nome in jedi:
    print(nome)

#Separador
print("-"* 70)

jedi2 = ["Yoda", "Luke", "Obi-Wan", "Anakin"]

#incluindo um valor digitado no final da lista
jedi2.append(input("Digite o nome de um jedi "))

for nome in jedi2:
    print(nome)