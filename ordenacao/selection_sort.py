import random
a = []

def troca(lista, val1, val2):
    lista[val1], lista[val2] = lista[val2], lista[val1]


def selection_sort(lista):
    global j 
    for i in range(0, len(a), 1):
        for j in range(i + 1 , len(a), 1):
            if(lista[j] < lista[i]):
                troca(lista, i, j)
        print(lista)
        

a = random.sample(range(100),50)
print(a)
selection_sort(a)

