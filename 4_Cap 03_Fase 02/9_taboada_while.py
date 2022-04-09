n = int(input("De qual número quer a taboada "))
taboada = 1

while taboada <= 10:
    mult = taboada * n
    print ("{} x {} é {}.".format(n, taboada, mult))
    taboada += 1

