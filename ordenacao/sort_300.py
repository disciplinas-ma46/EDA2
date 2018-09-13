import csv

nota = []

'''inserir = ['automoveis 1.0', 33.81]
with open(r'impostos.csv', 'a') as data:
    writer = csv.writer(data)
    writer.writerow(inserir)
'''
#data = csv.reader(open('impostos.csv', 'r', delim))
#next(data)  # Descarta o cabeçalho 
#imprimir primeira coluna

with open ("impostos.csv", "r") as f:
    dados = csv.reader(f, delimiter=";")
    next(dados) # Descarta o cabeçalho

    lista = list(dados)

for i in lista:
    del i[0]

print(lista)

#lista_ordenada = sorted(dados, )

#print(dados[0][0])

 