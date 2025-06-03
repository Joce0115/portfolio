# Jocelyn Garcia
# 01/23/2025
# create a list


# init
shoppingList = ["Shampoo", "Conditioner", "Chocolate", "Q-tips"] # empty

#function

#main
def shopping_list():
    global shoppingList
    print("Welcome to shopping list organizer")
    print("Try adding a few things to start:")

    while True:

        print("1. view shopping list\n2. add things \n3. remove item \n4. quit")
        #collecting Input
        try:
            ans = input("Type a number betweeen 1 and 4:")
            ans = int(ans)
        except:
            print("ERROR: Must type in a number")

        # process the information
        if ans == 1:
            print("Here is your movie watch list")
            print(shoppingList)
        if ans == 2:
            addItem = input("What item do you want to add to your list?: ")
            shoppingList. append(addItem)
            print("Sucessfuly added " + addItem)

        if ans == 3:
            removeItem = input ("What item do you want to remove from your list?: ")
            shoppingList.remove(removeItem)
            print("You have removed " + removeItem)
        if ans == 4:
            print(shoppingList)
            print("Thank you for using our app ")
            break
#main
shopping_list()


#jocelyn garcia
#01/27/2025
#magic 8 ball


#
#function
#main
# try except tutorial
try: # try to run this code
    x= input("Please enter a number between 1-10")
    x = int(x) #swapping x from a string to integer
except: # if there is an error do this instead of crashing
    print("ERROR: Must enter a number!`")
