#joce
#12/13/2024
#35condition challenge

#init


#Functions
def purchase(price):
    if price >= 100: #if the price is at 100 or more you get a discount of 10%
        print ("10% discount is applied") # tells you that you got the discount
    else:
        print("No discount is applied") # tells you that you didn't get the discount
#Main
purchase(110) # function being called and tested


#2 Temperature
#Init
#Functions
def temp(temp): # the function and telling you to input a temp when calling the function
    if temp >= 15 and temp <= 25:
        print("Safe temperature.") # telling you that the temperature is in between the safe temp
    else:
        print("Temperature out of range.") # the temp isn't within the safe temperature
#Main
temp(30) # calling function and testing it


#3 Two Numbers
#Init
#Functions
def number(x,y):
    if x > y: # telling you the first number is bigger than the second
        print("x is larger")
    elif x < y: # telling you that the second number is bigger than the first one
        print("y is larger")
    else:
        print("Both numbers are equal") # telling you that both number are equal to eachother
#Main
number(5,4)  #calling and testing out the function


#4 Divisibility

#Init
#Functions
def divisibility(num): # telling you that you have to input a number when you call the function
    if num % 3==0 or num % 5==0: # seeing if the the input of the user is divisible by 3 or 5
        print("Divisble by 3 or 5")
    else:
        print("Not divisible by 3 or 5") # tells you that the number is not divisible by 3 or 5
#Main
divisibility(15) # calling and testing out the function
