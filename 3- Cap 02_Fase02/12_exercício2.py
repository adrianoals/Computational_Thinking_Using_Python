valor_bruto= float(input("Digite o valor da viagem "))
categoria_assento = input("Digite o assento da viagem ").lower()
quantidade_de_viajantes = int(input("Digite a quantidade de viajantes "))
desconto = 0
desconto = float(desconto)
print(valor_bruto)

if categoria_assento == "economica":
    if quantidade_de_viajantes < 2:
        desconto = 0
    elif quantidade_de_viajantes == 2:
        desconto = 3/100
    elif quantidade_de_viajantes == 3:
        desconto = 4/100
    elif quantidade_de_viajantes >= 4:
        desconto = 5/100

if categoria_assento == "executiva":
    if quantidade_de_viajantes < 2:
        desconto = 0
    elif quantidade_de_viajantes == 2:
        desconto = 5/100
    elif quantidade_de_viajantes == 3:
        desconto = 7/100
    elif quantidade_de_viajantes >= 4:
        desconto = 8/100

if categoria_assento == "primeira classe":
    if quantidade_de_viajantes < 2:
        desconto = 0
    elif quantidade_de_viajantes == 2:
        desconto = 10/100
    elif quantidade_de_viajantes == 3:
        desconto = 15/100
    elif quantidade_de_viajantes >= 4:
        desconto = 20/100


valor_liquido = valor_bruto - (valor_bruto * desconto)
print(valor_liquido)
media_por_viajante = valor_liquido / quantidade_de_viajantes
print(media_por_viajante)
