#joce
#01/07/2025
#Rock,paper,scissors


#Int
import random
wins = 0 #Tracks player's wins
losses = 0  #Tracks player's losses
ties = 0  #Tracks player's ties

#function
def RPS(): # what the code is called
    global wins # how many times you have won
    global losses # how many times you have lost
    global ties # how many times you have tied
    print("Welcome to Rock Paper Scissors") # welcomes the player
    while True: #Infinite loop

        #step 1 collect players move
        print("What is your move?") # asking the player what their move is gonna be
        player = input ("Rock, Paper, Scissors") # inputs that the player is only able to put in
        player= player.capitalize() # if the player forgot to capatalize their input this code does it for them

        #step 2 generate a move for the computer
        computer = random.randint(1,3) # randomizing what input the program is gonna give
        if computer == 1: # 1= paper
            computer ="Paper"
            print("The computer picked Paper") # telling the player that the computer picked paper
        if computer == 2: # 2 = rock
            computer ="Rock"
            print("The computer picked Rock")# telling the player that the computer picked rock
        if computer == 3: # 3 = scissors
            computer ="Scissors"
            print("The computer picked Scissors")# telling the player that the computer picked scissors

        #step 3 tell player if they won or lost
        if player == "Paper" and computer == "Paper":
            print("tie") # telling the player that they tied with the computer
            ties = ties + 1 # telling player how many ties they have
        if player == "Paper" and computer == "Scissors":
            print("You Lost")# telling the player that they lost to the computer
            losses = losses + 1  # telling player how many times they lost
        if player == "Paper" and computer == "Rock":
            print("You WON!")# telling the player that they won against the computer
            wins = wins + 1 # telling player how many times they won
        if player == "Rock" and computer == "Rock":
            print("tie")# telling the player that they tied with the computer
            ties = ties + 1  # telling player how many ties they have
        if player == "Rock" and computer == "Paper":
            print("You Lost") # telling the player that they lost to the computer
            losses = losses + 1 # telling player how many times they lost
        if player == "Rock" and computer == "Scissors":
            print("You WON!") # telling the player that they won against the computer
            wins = wins + 1 # telling player how many times they won
        if player == "Scissors" and computer == "Scissors":
            print("tie")# telling the player that they tied with the computer
            ties = ties + 1  # telling player how many ties they have
        if player == "Scissors" and computer == "Rock":
            print("You Lost")# telling the player that they lost to the computer
            losses = losses + 1 # telling player how many times they lost
        if player == "Scissors" and computer == "Paper":
            print("You WON!") # telling the player that they won against the computer
            wins = wins + 1 # telling player how many times they won

    # Step 4 loop program until player wants to quit

        playagain = input ("Do you still want to play?") # asking player if they wanna play again to see if the program is gonna loop restart or if it is gonna break
        if playagain.lower() == "yes": # loop will restart if they say yes
            print("restarting....")
        else:
            print("Thank you for playing") # loop will not restart if they say no
            break

    #step 5 keep track of wins and losses
    print( "You have " + str(wins) + " wins") # telling the player thier score once they break the loop
    print ( "You have " + str(losses) + " losses")
    print ( "You have " + str(ties) + " ties")

#main
RPS() # calling the code
