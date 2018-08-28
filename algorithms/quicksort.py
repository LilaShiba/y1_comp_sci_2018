from random import randint
import random

def create_array(size=10,max=50):
    return [randint(0,max)for x in range(size)]

print(create_array())

def c_array(size=10, max=50):
    return random.sample(range(0,max),size)

print(c_array())
