#jocelyn garcia
#01/27/2025
#magic 8 ball


#int
import random
magic8ball_list = ["Yes", "Maybe", "No", "Definetly", "Possibly","Unfortunatly","Positive","Could be","Absalutly not","Affirmative","Potentially","Negative","Yup","God willing", "Nope"]
#import shake
#function
#main


# introduece
#ask the user for a question
# randmly display a response
# loop
#verify that user enteres a question


# yes: yes, definetly, of course, affirmative, yup
# maybe:maybe, possibaly, could be, potentially, god willing
# no: no, unfortunatly,absalutly not, negative, nope


#randomly display a response
#print("Shake...")
#time . sleepy(2)
#print("Shake...")
#time . sleepy(2)
#print("Shake...")
#time . sleepy(2)

def magic8_Ball():
    global magic8ball_list
    print("Welcome to Magic 8 Ball")
    while True:
        try:
            answer = input("Ask your question (Add question mark at the end of your question):")
            answer = answer.endswith("?")
            answer = int(answer)
        except:
            print("ERROR: Must type a question")

        answer = random.randint(1,15)
        if answer == 1:
            answer = "Yes"
            print("Yes")
        if answer == 2:
            answer = "Maybe"
            print("Maybe")
        if answer == 3:
            answer = "No"
            print("No")
        if answer == 4:
            answer = "Definetly"
            print("Definetly")
        if answer == 5:
            answer = "Possibly"
            print("Possibly")
        if answer == 6:
            answer = "Unfortunatly"
            print("Unfortunatly")
        if answer == 7:
            answer = "Positve"
            print("Positive")
        if answer == 8:
            answer = "Could be"
            print("Could be")
        if answer ==9:
            answer = "Absolutly not"
            print("Absolutly not")
        if answer == 10:
            answer = "Affirmative"
            print("Affirmative")
        if answer == 11:
            answer = "Potentially"
            print("Potentially")
        if answer == 12:
            answer = "Negative"
            print("Negative")
        if answer == 13:
            answer = "Yup"
            print("Yup")
        if answer == 14:
            answer = "God willing"
            print("God willing")
        if answer == 15:
            answer = "Nope"
            print("Nope")
        again =input("Would you like to ask another question?:")
        if again== "yes":
            print("Ask another question")
        else:
            print("Thank you for playing")
            break

#main
magic8_Ball()
