import numpy, random, matplotlib.pyplot as plt
# setup traveling salesman problem
cities = [random.sample(range(100),2) for z in range(50)]
print(cities)

x_axis = []
y_axis = []

for x,y in cities:
    x_axis.append(x)
    y_axis.append(y)
print(x_axis[1])
print(y_axis[1])

tour = random.sample(range(20),20)
print(tour)
# without the ts
plt.plot(x_axis,y_axis[:])
plt.show()
# show points
plt.scatter(x_axis, y_axis)
plt.show()

#
