n_transacoes = int(input("Informe quantas transações realizou durante o dia "))
soma_gastos = 0


for transacao in range(1, n_transacoes + 1):
    gastos = float(input("Informe o valor gasto na transação {}: ".format(transacao)))
    soma_gastos += gastos

print("O gasto total é de {}.".format(soma_gastos))
print("A média das transações é de {:.2f}".format(soma_gastos/n_transacoes))