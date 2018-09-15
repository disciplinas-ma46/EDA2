import csv
from math import floor 

nota = []
actual = 1
growing = 1
decreasing  = 0
i = 1

def number_per_group(number):
    return number/5

def populate_growing(lists):
    for i in range(0,4,1):
       lists[i].append(i)

'''
inserir = ['automoveis 1.0', 33.81]
with open(r'impostos.csv', 'a') as data:
    writer = csv.writer(data)
    writer.writerow(inserir)
'''
#data = csv.reader(open('impostos.csv', 'r', delim))
#next(data)  # Descarta o cabeçalho
#imprimir primeira coluna

with open ("impostos.csv", "r") as f:
    dados = csv.DictReader(f, delimiter=";")
    #next(dados) # Descarta o cabeçalho

    #lista = dados

    for line in dados:
        nota.append(list(line.values()))

nota.sort(key=lambda x: x[1], reverse=True)

qtd_per_group = number_per_group(len(nota))
decreasing = floor(qtd_per_group)

print("actual: %d growing: %d deacreasing: %d" %(actual, growing, decreasing))

for line in nota:
    if(growing > floor(qtd_per_group)):
        growing = 1
        actual += 1
        pass
    
    if(decreasing < 1):
        decreasing = floor(qtd_per_group)
        actual += 1
        pass

    if(actual == 1 or (len(nota) - i) < floor(qtd_per_group) and decreasing == floor(qtd_per_group)):
        line.append(growing)
        growing += 1
    elif(actual > 1):
        line.append(decreasing)
        decreasing -= 1
    print("actual: %d growing: %d deacreasing: %d" %(actual, growing, decreasing))
    i += 1

nota.sort(key=lambda x: x[2])

for line in nota:
    print(line)

#lista_ordenada = sorted(dados, )

#print(dados[0][0])


#for i in lista:
#    del i[0]
