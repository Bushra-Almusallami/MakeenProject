from random import randint

rang=randint(1,100)
print(rang)
number=int(input("Enter number between 1 and 100:"))

for x in range(5):
    if (number <1 or number >100):
        print("outside the range!")
        number=int(input("Enter number between 1 and 100:"))
    elif(number >rang):
        print("Go lower")
        number=int(input("Enter number between 1 and 100:"))
    elif(number <rang):
        print("Go higher")
        number=int(input("Enter number between 1 and 100:"))
    else:
        print("Congratulation")
    
