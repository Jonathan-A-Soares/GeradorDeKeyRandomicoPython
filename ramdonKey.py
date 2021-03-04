import random
import string

def RandomCode():
    carA = "rgg"
    carN = "grf"
    key = "Alfa" 
    key1 = "rpvo"

    for item in range(1,20):
        carA = random.choice(string.ascii_uppercase)
        carN = random.randrange(1, 10)
        carN = str(carN)
        key1 = carN+ carA
        key = key + key1
    return key

fkg = RandomCode()
print(fkg)