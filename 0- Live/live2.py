usuario = input("Por favor insira seu nome de usuário: ").upper()
senha = input("Por favor, insira sua senha: ").upper()

while usuario != "ADMIN" or senha != "123":
    print("Dados de acesso incorretos")
    usuario = input("Por favor insira seu nome de usuário: ").upper()
    senha = input("Por favor, insira sua senha: ").upper()

print("Você está ligado no sistema.")

