notas = []

opcao = -1

while opcao != 4:
    print("1 - Informar notas \n2 - Exibir notas \n3 - Calcular média \n4 - Sair")
    print("."*70)
    opcao = int(input("Escolha sua opcao "))
    print("."*70)

    if opcao == 1:
        notas.append(float(input("Digite a nota ")))
        print("."*70)

    elif opcao == 2:
        for x in notas:
            print(x)
        print("."*70)    
    
    elif opcao == 3:
        print(sum(notas)/len(notas))
        print("."*70)





