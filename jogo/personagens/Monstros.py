import random 

def enemy1():
    global hpm 
    hpm = random.randint(10, 100)
    statusm = { "fo" : random.randint(5, 25),
                "de" : random.randint(5, 10)
                }
enemy1()