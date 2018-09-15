import csv

nota = []

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

populate_growing(nota)

print(nota)
#lista_ordenada = sorted(dados, )

#print(dados[0][0])


#for i in lista:
#    del i[0]
