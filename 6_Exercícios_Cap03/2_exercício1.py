# Aluno: Adriano Lima Santos
# RM: 95667
"""
1 – Você foi procurado por um aluno do curso de Produção Multimídia do FIAP ON 
para desenvolver um trabalho em parceria: um serviço em que as pessoas possam 
usar um estúdio profissional para gravar seus vídeos para o YouTube com máxima 
qualidade. O serviço ganha dinheiro por meio de um sistema de assinaturas e de 
um bônus calculado por uma porcentagem sobre o faturamento que o canal do 
cliente obteve ao longo do ano.

Sua tarefa é criar um algoritmo que receba o tipo de assinatura do cliente, 
o faturamento anual dele e que calcule e exiba qual o valor do bônus que o 
cliente deve pagar a vocês. A tabela abaixo mostra a porcentagem de acordo 
com cada nível de assinatura:

Nível          Porcentagem sobre o faturamento

Basic                       30%

Silver                      20%

Gold                        10%

Platinum                     5%

"""
assinatura = input("Informe sua assinatura: B-Basic, S- Silver, G- Gold e P-Platinum ").upper()

if assinatura != "B" and assinatura != "S" and assinatura != "G" and assinatura != "P":
    print("Não possui assinatura.")

else:
    faturamento_anual = float(input("Informe seu faturamento anual: "))
    bonus = 0

    if assinatura == "B":
        porcentagem_sobre_faturamento = 0.3
        bonus = faturamento_anual * porcentagem_sobre_faturamento

    elif assinatura == "S":
        porcentagem_sobre_faturamento = 0.2
        bonus = faturamento_anual * porcentagem_sobre_faturamento

    elif assinatura == "G":
        porcentagem_sobre_faturamento = 0.1
        bonus = faturamento_anual * porcentagem_sobre_faturamento

    elif assinatura == "P":
        porcentagem_sobre_faturamento = 0.05
        bonus = faturamento_anual * porcentagem_sobre_faturamento

    print("O cliente deve pagar um bonus de R${0:.2f}".format(bonus))