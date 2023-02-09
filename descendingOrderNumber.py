import random #put that in for testing different numbers easily
# This is a dice machine that takes rand numbers and sorts them from biggest to smallest
def descending_order(num):
    
    nim = str(num)
    nam = sorted(nim)
    nom = nam[::-1]
    nem = ''.join(nom)
       
    return nem

wurf = random.randint(20000,99000) # this is just for testing
print(descending_order(wurf))
