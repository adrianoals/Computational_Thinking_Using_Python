#playstation 
#xbox
#nintendo

voto1 = input ("Escolha qual dos consoles prefere (P) para Playstation, (X) para Xbox e (N) para Nintendo ")
voto2 = input ("Escolha qual dos consoles prefere (P) para Playstation, (X) para Xbox e (N) para Nintendo ")
voto3 = input ("Escolha qual dos consoles prefere (P) para Playstation, (X) para Xbox e (N) para Nintendo ")
voto4 = input ("Escolha qual dos consoles prefere (P) para Playstation, (X) para Xbox e (N) para Nintendo ")
voto5 = input ("Escolha qual dos consoles prefere (P) para Playstation, (X) para Xbox e (N) para Nintendo ")

playstation =  0
xbox = 0
nintendo = 0

if voto1.upper() == "P":
    playstation += 1
elif voto1.upper() == "X":
    xbox += 1
elif voto1.upper() == "N":
    nintendo += 1
else:
    print("O colaborador digitou um console inexistente voto desconsiderado.")

if voto2.upper() == "P":
    playstation += 1
elif voto2.upper() == "X":
    xbox += 1
elif voto2.upper() == "N":
    nintendo += 1
else:
    print("O colaborador digitou um console inexistente voto desconsiderado.")

if voto3.upper() == "P":
    playstation += 1
elif voto3.upper() == "X":
    xbox += 1
elif voto3.upper() == "N":
    nintendo += 1
else:
    print("O colaborador digitou um console inexistente voto desconsiderado.")

if voto4.upper() == "P":
    playstation += 1
elif voto4.upper() == "X":
    xbox += 1
elif voto4.upper() == "N":
    nintendo += 1
else:
    print("O colaborador digitou um console inexistente voto desconsiderado.")

if voto5.upper() == "P":
    playstation += 1
elif voto5.upper() == "X":
    xbox += 1
elif voto5.upper() == "N":
    nintendo += 1
else:
    print("O colaborador digitou um console inexistente voto desconsiderado.")

print("Playstation: {} \nX-box: {} \nNintendo : {}". format(playstation, xbox, nintendo))


if playstation > nintendo and playstation > xbox:
    print("O console escolhido é o Playstation.")
elif nintendo > playstation and nintendo > xbox:
    print("O console escolhido é o Nintendo.")
elif xbox > nintendo and xbox > nintendo:
    print("O console escolhido é o X-box.")
else:
    print("Houve empate entrar em contato com a direção.")
    