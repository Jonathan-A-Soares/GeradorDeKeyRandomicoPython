import random
import string

def RandomCode():
    carA = "rgg"
    carN = "grf"
    key = "Alfa" 
    key1 = "rpvo"
    

    
    for item in range(1,10):
        contador = 0
        indC = random.randrange(0, 4)
        indN = random.randrange(0, 4)
        indNE = random.randrange(33, 63)
        indNE2 = random.randrange(91, 95)
        

        for numero in range(1,indN):
            carN = random.randrange(1, 10)
            end = chr(indNE)
            end2 = chr(indNE2)
            carN = str(carN)
            key = key + carN 
            while (contador < 1):
                key = key + end + carN + end2
                contador   = contador + 1

        
        indNE = random.randrange(33, 63)
        indNE2 = random.randrange(91, 95)
        

        for caracter in range(1,indC):
            carA = random.choice(string.ascii_uppercase)
            end1 = chr(indNE)
            end2 = chr(indNE2)
            key = key + carA 
            while (contador < 1):
                key = key + end + carN + end2
                contador   = contador + 1

    
     
    return key

fkg = RandomCode()
print(fkg)