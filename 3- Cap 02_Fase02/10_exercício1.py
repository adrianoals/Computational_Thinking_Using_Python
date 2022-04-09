#Exercício BPM

bpm = int(input("Digite seu bpm "))
idade = int(input("Informe sua idade "))

if idade <= 2:
    if bpm >= 120 and bpm <= 140:
        print ("BPM dentro da faixa adequada.")
    else:
        print ("BPM fora da faixa adequada")

elif idade >= 8 and idade <= 17:
    if bpm >= 80 and bpm <= 100:
        print ("BPM dentro da faixa adequada.")
    else:
        print ("BPM fora da faixa adequada")


