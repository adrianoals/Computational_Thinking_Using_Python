# Aluno: Adriano Lima Santos
# RM: 95667
"""
3 – Muitos professores preferem adotar modelos diferentes de provas quando dão aulas 
para turmas muito grandes. Por essa razão, a escola de inglês JoWell Sant’ana, 
em que todas as turmas são compostas por 50 alunos, solicitou que você criasse um sistema 
capaz de atender ao seguinte requisito: o professor deve digitar primeiro as notas dos 25 
alunos que têm número ímpar na chamada (1, 3, 5..., 47, 49) e depois as notas dos 25 alunos 
que têm número par (2, 4, 6..., 48, 50). O sistema deve calcular e exibir a média de cada uma 
das metades da sala e informar, ao final, qual delas teve a maior nota.

Há ainda um pedido especial do mantenedor: para que os professores não se confundam,
ao digitar cada uma das notas deve ser exibida uma mensagem no seguinte padrão:

VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES (ou ímpares, quando for o caso).
POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO x.

"""
soma_notas_impares = 0
soma_notas_pares = 0

for impar in range(1, 50, 2):
    print ("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS IMPARES")
    notas = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: " .format(impar)))
    soma_notas_impares = soma_notas_impares + notas

print("-" *70)

for par in range(2, 50, 2):
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES")
    notas = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: " .format(par)))
    soma_notas_pares = soma_notas_pares + notas

print("-" *70)
media_impares = soma_notas_impares / 25
print("A média das notas dos alunos ímpares é: {:.2f}" .format(media_impares))

media_pares = soma_notas_pares / 25
print ("A média das notas dos alunos pares é: {:.2f}".format(media_pares))

print("-" *70)

if media_impares > media_pares:
    print("Os alunos impares tiveram as melhores notas")
else:
    print("Os alunos pares tiveram as melhores notas")

print("-" *70)
