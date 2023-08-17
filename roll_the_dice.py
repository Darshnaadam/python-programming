import random

def rolldice(min,max):
    print(f"Rolling th dice.....")
    number = random.randint(min,max)
    print(f"Your number : {number}")
    
rolldice(1,6)