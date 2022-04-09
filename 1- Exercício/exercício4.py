print ("Esse programa calcula a velocidade média de um patinete")
distancia = input("Qual foi a distancia percorrida do patinete? ")
tempo = input("Quantos minutos o patinete percorreu essa distancia ")

velocidade_media = float(distancia) / float(tempo)

print("O patinete atingiu a velocidade de %.2f m/min" %velocidade_media)
print("O patinete atingiu a velocidade de", velocidade_media)
print("O patinete atingiu a velocidade de {0:.0f} m/min" .format(velocidade_media))


