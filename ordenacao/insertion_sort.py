import random

a = []
aux = 0

def troca (lista, val1, val2):
    lista[val1], lista[val2] = lista[val2], lista[val1]

def insertion_sort(lista):
    aux = lista[1]
    pos_aux = 1
    i = 0

    while(True):
        i = pos_aux
        print("enlace: ", i)
        while(aux < lista[i - 1] and i != 0):
            troca(lista, i, i-1)
            i -= 1
            print(i)
        print(lista)
        if(pos_aux != len(lista) - 1):
            pos_aux += 1
            aux = lista[pos_aux]
        else:
            break



a = random.sample(range(100),50)
print(a)
insertion_sort(a)