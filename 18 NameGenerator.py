#Joce
#10/18/2024
#Name Generator


#Init
#function
def Name_Generator(): # making up a name
    choose = (input("Please pick Warm or Cold:")) #picking between these two options
    if choose == "Warm": #it's gonna give you more options

        choose = (input("Pick a season you prefer Summer or Spring:"))# giving more option to decide name
        if choose== "Summer": # result to option
            choose = (input("Pick which one you like more Land or Water?:")) # giving more option to decide name
            if choose == "Water":
                print("You are Moana") # name that you got after picking the last option
            elif choose == "Land":
                print("You are Jasmine")  # name that you got after picking the last option
        elif choose == "Spring":
            choose = (input("Pick between losing your Hair or Voice?:")) # giving more option to decide name
            if choose == "Voice":
                print("You are Ariel")  # name that you got after picking the last option
            elif choose == "Hair":
                print("You are Rapunzel")  # name that you got after picking the last option

    else:  # what options you would get if you picked cold
        choose = (input("Pick a season you prefer Fall or Winter?"))  #picking between these two options
        if choose == "Fall":
            choose = (input("Pick between Cleaning or Cooking?")) # giving more option to decide name
            if choose == "Cooking":
                print("You are Tiana") # name that you got after picking the last option
            elif choose == "Cleaning":
                print("You are Cinderella")  # name that you got after picking the last option
        elif choose == "Winter":
            choose = (input("Which do you like more Eating or Reading?"))# giving more option to decide name
            if choose == "Eating":
                print("You are Elsa")  # name that you got after picking the last option
            elif choose == "Reading":
                print("You are Belle")  # name that you got after picking the last option

#Main
Name_Generator() # name you end up with
