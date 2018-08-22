import random

list_numbers = random.sample(range(1, 101), 20)    #creating a list in range 0 to 100 
list_numbers.sort()    # ordering
print(list_numbers)

search_number = random.choice(list_numbers)
print(search_number)

