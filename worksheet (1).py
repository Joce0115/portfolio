#Jocelyn Garcia
#11/12/2024
#

#init
import random


#function
def Guessing_Game():
    guess = int(input("Ener Guess")) #integer
    secret= random.randint(0,10) #integer
    if guess==secret:
        print("You won")
    else:
        print("You lost")
    if guess>secret:
        print("The number you picked is higher")
    if guess<secret:
        print("The number you picked is lower")
    print(str(secret) + " was the correct answer")
    if guess!=secret:
        print("Do you want to play again?")


#Main
Guessing_Game()
