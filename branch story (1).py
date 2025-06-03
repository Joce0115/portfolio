#jocelyn garcia
#01/16/2025
#branching out story

#init
score = 0


#function
def doras_adventure(presents):
     print("Welcome to Dora's Adventure:")
     print("Today grandma sent us on a adventure to deliver a special item!!!:")
     print("Grandma said that we are gonna collect pieces to the item as we continue the journey!:")
     global score
     while True:
        for i in range(presents):
            print("First things first what should we wear on our adventure?")
            print("pick a number from 1-3")
            player = int(input("1 or 2"))
            if player == "1": # outfit 1
                print("the outfit you will wear is gonna be a pink shirt, orange pants, and white shoes.")
                score = score + 50 # score for picking this outfit
                print("You gained " + str(score) + " points")

            if player =="2":# outfit 2
                print("You will wear a blue shirt, white pants, and black shoes.")
                score = score + 20 # score for picking this outfit
                print("You gained " + str(score) + " points")

            print("Now that you picked your outfit we are gonna start")
            print("our first stop on the list is the ribbon shop")
            print("pick a color for the ribbon")
            ribbon= input("Please enter a color:")
            score = score + 25 # score
            print("the ribbon is " + str(ribbon) + " and you have earned " + str(score) + " points")

            print("Now that we have a ribbon we need to go to our next stop")
            print("Our next stop is to get wrapping paper")
            print("what kind of wrapping paper do you want?")
            paper =  input("Enter a design or color for the wrapping paper:")
            score = score + 30 # score
            print("the wrapping paper is " + str(paper) + " and you have earned " + str(score) + " points")

            print("We need a bow now")
            print("Lets go to the bow show")
            print("Pick a bow that matches the rest of the decorations")
            bow = input("Enter a color the bow should be")
            score = score + 40 # score
            print("the bow is " + str(bow) + " and you have earned " + str(score) + " points")

            print("now decorate the box")
            score = score + 25 # score
            print("Now that you finished decorating the box you have to deliver it" + " and you have earned " + str(score) + "points")
            print("you forgot how to get to your grandmas house")
            print("pick to go left or right")
            pick = input("left or right")
            if pick == "left" :
                print("You made it to grandmas house and completed the mission")
                score = score+ 40 # score

            else:
                print("You didn't make it to grandmas house and she was upset")
                score = score - score
                print("you didn't earn any point becuase you didn't complete the journey ")

        again = input("Would you like to play again?:")
        if again == "yes":
                print("Restarting...")
        else:
                print("Thank you for playing")
        break



#main
doras_adventure(2)

