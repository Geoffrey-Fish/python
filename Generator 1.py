import random

def Data():
    for i in range(10):
        yield random.randint(1,10)
#this is a random number generator, it gives 10 numbers
for num in Data():
    print(num)
