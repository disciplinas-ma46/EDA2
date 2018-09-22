import csv
from math import floor

people = []
actual = 1
growing = 1
decreasing  = 0
i = 1

def number_per_group(number):
    return number/5

def populate_growing(lists):
    for i in range(0,4,1):
       lists[i].append(i)

with open ("impostos.csv", "r") as f:
    dados = csv.DictReader(f, delimiter=",")
    #next(dados) # Descarta o cabeçalho

    for line in dados:
        people.append(list(line.values()))

people.sort(key=lambda x: x[1], reverse=True)

qtd_per_group = number_per_group(len(people))
decreasing = floor(qtd_per_group)

print("actual: %d growing: %d deacreasing: %d" %(actual, growing, decreasing))

for line in people:
    if(growing > floor(qtd_per_group)):
        growing = 1
        actual += 1
        pass

    if(decreasing < 1):
        decreasing = floor(qtd_per_group)
        actual += 1
        pass

    if(actual == 1 or (len(people) - i) < floor(qtd_per_group) and decreasing == floor(qtd_per_group)):
        line.append(growing)
        growing += 1
    elif(actual > 1):
        line.append(decreasing)
        decreasing -= 1
    print("actual: %d growing: %d deacreasing: %d" %(actual, growing, decreasing))
    i += 1

people.sort(key=lambda x: x[2])

c = csv.writer(open("trezentos_grupos.csv", "w"))
c.writerow(["Nome","Nota","Grupo"])

for line in people:
    c.writerow(line)
    
