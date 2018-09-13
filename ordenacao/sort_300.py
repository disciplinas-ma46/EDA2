import csv
inserir = ['automoveis 1.0', 33.81]
with open(r'impostos.csv', 'a') as data:
    writer = csv.writer(data)
    writer.writerow(inserir)

data = csv.reader(open('impostos.csv', 'r')) 
#imprimir primeira coluna 
for rows in data: 
    print rows 