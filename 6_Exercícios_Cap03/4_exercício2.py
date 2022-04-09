# Aluno: Adriano Lima Santos
# RM: 95667
"""
2 – Os alunos da sua turma fizeram uma votação para escolher qual dia da semana 
é o melhor para a realização das lives. Desenvolva um programa em que o usuário
informe a quantidade de votos que cada um dos 5 dias da semana (segunda-feira,
terça-feira, quarta-feira, quinta-feira e sexta-feira) obtiveram, verifique e 
exiba qual dia foi o escolhido.

"""

quantidade_de_alunos = 5
segunda_feira = 0
terça_feira = 0
quarta_feira = 0
quinta_feira = 0
sexta_feira = 0

for x in range(quantidade_de_alunos):
    print("Informe o melhor dia da semana para realização das lives.")
    print(" 1- Para segunda-feira \n 2- Para terça-feira \n 3- Para quarta-feira \n 4- Para quinta-feira \n 5- Para sexta-feira")
    voto = (input("Informe seu voto: "))

    if voto == "1":
        segunda_feira = segunda_feira + 1
    elif voto == "2":
        terça_feira = terça_feira + 1
    elif voto =="3":
        quarta_feira += 1
    elif voto =="4":
        quinta_feira += 1
    elif voto =="5":
        sexta_feira += 1
    print("-" * 70)

#Número de votos
print("Segunda-feira: {}, Terça-feira: {}, Quarta-feira: {}, Quinta-feira: {}, Sexta-feira: {}".format(segunda_feira, terça_feira, quarta_feira, quinta_feira, sexta_feira))

#Texto informando o mais votado
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