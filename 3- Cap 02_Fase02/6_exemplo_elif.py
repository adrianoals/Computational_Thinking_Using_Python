pontuação = input ("Insira a pontuação do cliente ")
pontuação = int(pontuação)

if pontuação >= 1000:
    print ("O cliente tem direito a receber mais 3gb na sua franquia de internet!")

elif pontuação >= 500:
    print ("O cliente tem direito a receber mais 1,5gb na sua franquia de internet!")
    
elif pontuação >= 200:
    print ("O cliente tem direito a receber mais 500mb na sua franquia de internet!")

else:
    print ("O cliente não recebera bônus.")

