#Sequencia de Fibonacci

quantidade_de_elementos = 7
anterior1 = 1
anterior2 = 0 

for n_elementos in range(1, quantidade_de_elementos + 1, 1):
    atual = anterior1 + anterior2
    anterior1 = anterior2
    anterior2 = atual
    print(atual)
