usuario = input("Por favor insira seu nome de usuário: ").upper()
senha = input("Por favor, insira sua senha: ").upper()

if usuario == "ADMIN" and senha == "123":
    print("Você está ligado no sistema.")
else:
    print("Dados de acesso incorretos")

