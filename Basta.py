#Jocelyn Garcia
#02/25/2025
#basta



#Int
alfabeto = ["A","B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
import random


#Function
def Basta():
    global alfabeto
    print("Bienvenidos jugadores")
    print("Hay que ver que letra les va a tocar")

    while True:
        print("pon 1 para empezar. pon 2 para ver las letra que faltan. Pon 3 para empezar otra vez. Pon 4 para para de jugar")

        try:
            numero= input("Pon un numero:")
            numero= int(numero)
        except:
            print("ERROR: Tienes que poner un numero")

        if numero == 1:
            print("Hay que comensar a jugar")
            random.choice(alfabeto)
            print(random.choice)
            alfabeto.remove(random.choice)
            #print(random.randint(alfabeto))
           # print()# STUCK HERE to pick a letter and then remove it

        if numero == 2: # letras que faltan
            print("Aqui estan las letras que quedan")
            print(alfabeto)

        if numero == 3: # esmezar de nuevo con toda las letras
            print(alfabeto)

        if numero == 4:
            print(alfabeto) # puedo quitar el codigo para imprimir solo quiro que se termine el juego
            break

#Main
Basta()
