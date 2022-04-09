#criação de uma lista com os nomes dos Jedi
jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]
#incluindo um valor em uma posição específica da lista
jedi.insert(2, "Luminara")
#A variável assumirá cada um dos valores da lista
for nome in jedi:
    #para cada volta do loop, exibir o valor assumido
    print(nome)

#separador 
print("-"*70)
print("-"*70)

#criação de uma lista com os nomes dos Jedi
jedi2 = ["Yoda", "Luke", "Obi-Wan", "Anakin"]
#incluindo um valor pelo usuário em uma posição específica da lista
jedi2.insert(2, input("Digite o nome de um Jedi "))
#A variável assumirá cada um dos valores da lista
for nome in jedi2:
    #para cada volta do loop, exibir o valor assumido
    print(nome)