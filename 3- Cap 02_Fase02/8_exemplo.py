compra = float(input("Digite o valor da compra "))
desconto = input("Vai utilizar desconto? S-Sim ou N-Não ").upper()

if desconto == "S":
    cupom = input("Digite cumpom do desconto ").upper()
    if cupom == "NIVER10":
        valor_final = compra * 0.9
        print ("O valor da sua compra é {}".format(valor_final))
else:
    print("O valor da sua compra é {}".format(compra))

