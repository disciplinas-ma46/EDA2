import csv

nota = []

'''
inserir = ['automoveis 1.0', 33.81]
with open(r'impostos.csv', 'a') as data:
    writer = csv.writer(data)
    writer.writerow(inserir)
'''
#data = csv.reader(open('impostos.csv', 'r', delim))
#next(data)  # Descarta o cabeçalho 
#imprimir primeira coluna

with open ("arquivo.csv", "r") as f:
    dados = csv.DictReader(f, delimiter=",")
    next(dados) # Descarta o cabeçalho

    #lista = dados

    for line in dados:
        nota.append(list(line.values()))

    for row in nota:
        print(row[1])
#lista_ordenada = sorted(dados, )

#print(dados[0][0])


#for i in lista:
#    del i[0]