import random

while True:
    print('''1. Roll the dice       2. Exit        ''')
    user = int(input("what do you want to do: "))
    if user==1:
        number = random.randint(1,6)
        print(number)
    
    else :
        break