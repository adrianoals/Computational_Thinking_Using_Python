#Exercício BPM

bpm = int(input("Digite seu bpm "))
idade = int(input("Informe sua idade "))

if idade <= 2 and 120 <= bpm <= 140: 
    print ("BPM dentro da faixa adequada.")

elif 2 <= idade < 8:
    print("Sem informações sobre seu BPM.")

elif 8 <= idade <= 17 and 80 <= bpm <= 100:    
    print ("BPM dentro da faixa adequada.")

elif 70 <= bpm <= 80:
    print("BPM de adulto sedentario.")

elif 50 <= bpm <= 60:
    print("BPM de idoso.")

else:
    print ("BPM fora da faixa adequada")

    