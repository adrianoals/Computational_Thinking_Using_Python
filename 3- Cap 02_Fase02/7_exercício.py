"""
O doutor Henry Jones Junior estabeleceu uma regra com seus alunos 
da disciplina de Arqueologia: todos os que obtiverem nota maior 
que 8,5 na sua prova semestral serão convidados para uma visita 
de campo na América do Sul.

Nosso programa deve solicitar o e-mail e a nota do aluno, exibindo a 
mensagem "Enviando Convite" caso a nota do aluno satisfaça a condição 
proposta.

Resolva utilizando apenas If simples e converta para float
"""

#solicitando os dados do aluno
email_aluno = input("Informe seu e-mail ")
nota_aluno = input("Informe sua nota ")

#convertendo para float
nota_aluno = float(nota_aluno)

if nota_aluno >= 8.5:
    print("Enviando e-mail para {}".format(email_aluno))
