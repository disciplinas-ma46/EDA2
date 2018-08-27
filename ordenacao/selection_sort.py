import random
a = []
j = 0
a = random.sample(range(10),3)

print(a)

def selection_sort():
    global j
    for i in range(0, len(a), 1):
        #actual = a[i]

        for j in range(i ,0, -1): 
            a[j-1], a[j] = a[j-1] , a[j]
        

selection_sort()


b = 2
c = 3

b,c = c,b
print(b,c)
