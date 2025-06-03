#Heading
#Initialize
gamesList = ["Roblox","Fortnite","LoL","Valorant","Overwatch"] #Empty
#Functions
def gameList1():
    global gamesList
    print("Welcome to the Games List Organizer!")
    print("With this game you customize your game(s) list.")
    while True:
        print("1.View List\n2.Add Game\n3.Remove Game\n4.Quit")
        ans = input("Type a number between 1 and 4: ")
        ans = int(ans)
        if ans == 1:
            print("Heres your current game list")
            print(gamesList)
        if ans == 2:
            addGame = input("What game do you want to add?")
            gamesList.append(addGame)
            print("Sucessfully added " + addGame)
        if ans == 3:
            subGame = input("What game do you want to remove?")
            gamesList.remove(subGame)
            print("Sucessfully removed " + subGame)
        if ans == 4:
            print(gamesList)
            break
#Main
gameList1()
