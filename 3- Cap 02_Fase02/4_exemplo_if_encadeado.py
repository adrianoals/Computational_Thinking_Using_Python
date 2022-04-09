rm = input("Digite seu RM ")
idade = input("Digite sua idade ")
if int (idade) >= 18:
    print("Sua participação foi autorizada, aluno do RM {}".format(rm))
    print ("Mais informações serão enviadas para seu e-mail cadastrado")
else:
    autorizado = input("Você possui autorização dos responsáveis? S-Sim ou N-Não ")
    if autorizado == "S":
        print ("Sua participação foi autorizada, aluno RM {}" .format(rm))
        print ("Mais informações serão enviadas para o e-mail do responsável")
    else:
        print ("Sua participação não foi autorizada por causa de sua idade.")