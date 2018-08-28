import random
my_list = [1,2,3,4,5];
# single
tour = random.sample(range(25),15)
# double
cities = [random.sample(range(50), 2) for x in range(15)]

#for x in my_list[::-1]:
#    print(x)

record = 0
for i in range(len(cities)):
    for j in range(len(cities[i])):
        if cities[i][j] > record:
            record = cities[i][j]
    print(record)
