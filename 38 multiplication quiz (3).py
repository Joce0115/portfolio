#joce
#date: 01/09/2025
#multiplcation quiz



# 1. Welcome the user to the game and structure your code
# 2. Use the random library to generate a random multiplication problem and allow the user to answer it.
# 3. Check to see if the user's answer is correct and update the score accordingly
# 4. Use a loop to repeat the process (Let's start with a quiz with 5 questions)
# 5. Give the user their final score


#Init
import random
correct= 0 #Tracks player's right answers
wrong= 0 #Tracks player's wrong answers

#function

#main
def multiplication_game(questions):
    print("Welcome to multiplication quiz!") # welcoming players
    global correct # how many questions you got right
    global wrong # how many questions are wrong
    while True:
        for i in range(questions):
            number1 = (random.randint(0,15)) # the first digit
            number2 = (random.randint(0,15)) # the second digit
            print(str(number1) + " * " + str(number2)) # giving the user the equation

            user_answer = int(input("please enter your answer:")) # the users answer
            answer = number1 * number2 # the correct answer
            if user_answer == answer:
                print("correct") # telling the user they got the question right
                correct = correct + 1 # telling them the number of questions they got right
                print("you have answered " + str(correct) + " correctly") # updating the user on their correct answers
            else:
                print("wrong") # tellling the used they got the question wrong
                wrong = wrong + 1
                print(answer) # letting the user know the correct answer to the equation

        again = input("Would you like to practice more?: ") # asking the player if they wanna practice more
        if again == "yes": # if the user doesn't want to play anymore the practice ends
            print("Restarting...")
        else:
            print("Thank you for playing") # saying good bye to the player
            break #ending the loop

#main
multiplication_game(5) # calling the code and looping it 5 times
