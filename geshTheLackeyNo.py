import random

def start_game():
    print("welcom to the game.")
    print("gess the no. from 1 - 100")
    n=random.randint(1,100)

    while True:
        user= int(input("enter a no :- "))
        if user == n :
            print("you gess the no.", n)
            break
        elif user < n:
            print("too low")
        else:
            print("too high")

loop = input("do you want to play this Game? (yes/no): ")
while loop.lower() == "yes":
    start_game()
    loop = input("do you want to play again? (yes/no): ")

