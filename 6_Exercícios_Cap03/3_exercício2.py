# Aluno: Adriano Lima Santos
# RM: 95667
"""
2 – Os alunos da sua turma fizeram uma votação para escolher qual dia da semana 
é o melhor para a realização das lives. Desenvolva um programa em que o usuário
informe a quantidade de votos que cada um dos 5 dias da semana (segunda-feira,
terça-feira, quarta-feira, quinta-feira e sexta-feira) obtiveram, verifique e 
exiba qual dia foi o escolhido.

"""

#Resolução apenas utilizando IFS


print("Informe o melhor dia da semana para realização das lives.")
print(" 1- Para segunda-feira \n 2- Para terça-feira \n 3- Para quarta-feira \n 4- Para quinta-feira \n 5- Para sexta-feira")

voto1 = (input("Informe seu voto: "))
voto2 = (input("Informe seu voto: "))
voto3 = (input("Informe seu voto: "))
voto4 = (input("Informe seu voto: "))
voto5 = (input("Informe seu voto: "))

segunda_feira = 0
terça_feira = 0
quarta_feira = 0
quinta_feira = 0
sexta_feira = 0

#Voto aluno 1
if voto1 == "1":
    segunda_feira = segunda_feira + 1
elif voto1 == "2":
    terça_feira = terça_feira + 1
elif voto1 =="3":
    quarta_feira += 1
elif voto1 =="4":
    quinta_feira += 1
elif voto1 =="5":
    sexta_feira += 1

#Voto aluno 2
if voto2 == "1":
    segunda_feira = segunda_feira + 1
elif voto2 == "2":
    terça_feira = terça_feira + 1
elif voto2 =="3":
    quarta_feira += 1
elif voto2 =="4":
    quinta_feira += 1
elif voto2 =="5":
    sexta_feira += 1

#Voto aluno 3
if voto3 == "1":
    segunda_feira = segunda_feira + 1
elif voto3 == "2":
    terça_feira = terça_feira + 1
elif voto3 =="3":
    quarta_feira += 1
elif voto3 =="4":
    quinta_feira += 1
elif voto3 =="5":
    sexta_feira += 1

#Voto aluno 4
if voto4 == "1":
    segunda_feira = segunda_feira + 1
elif voto4 == "2":
    terça_feira = terça_feira + 1
elif voto4 =="3":
    quarta_feira += 1
elif voto4 =="4":
    quinta_feira += 1
elif voto4 =="5":
    sexta_feira += 1

#Voto aluno 5
if voto5 == "1":
    segunda_feira = segunda_feira + 1
elif voto5 == "2":
    terça_feira = terça_feira + 1
elif voto5 =="3":
    quarta_feira += 1
elif voto5 =="4":
    quinta_feira += 1
elif voto5 =="5":
    sexta_feira += 1

#Número de votos
print("Segunda-feira: {}, Terça-feira: {}, Quarta-feira: {}, Quinta-feira: {}, Sexta-feira: {}".format(segunda_feira, terça_feira, quarta_feira, quinta_feira, sexta_feira))

if segunda_feira > terça_feira and segunda_feira > quarta_feira and segunda_feira > quinta_feira and segunda_feira > sexta_feira:
    print("O dia mais votado foi Segunda-Feira.")

elif terça_feira > segunda_feira and terça_feira > quarta_feira and terça_feira > quinta_feira and terça_feira > sexta_feira:
    print("O dia mais votado foi Terça-Feira.")

elif quarta_feira > segunda_feira and quarta_feira > terça_feira and quarta_feira > quinta_feira and quarta_feira > sexta_feira:
    print("O dia mais votado foi Quarta-Feira.")

elif quinta_feira > segunda_feira and quinta_feira > terça_feira and quinta_feira > quarta_feira and quinta_feira > sexta_feira:
    print("O dia mais votado foi Quinta-Feira.")

elif sexta_feira > segunda_feira and sexta_feira > terça_feira and sexta_feira > quarta_feira and sexta_feira > quinta_feira:
    print("O dia mais votado foi Sexta-Feira.")
else:
    print("Aguardar a direção, votação não obteve um resultado válido.")





