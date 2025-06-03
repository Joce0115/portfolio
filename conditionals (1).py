#Jocelyn Garcia
#10/11/2024
#conditionals statements

#Init
#functions
#conditionals statements

#Init
#functions
#This function checks whether you are eligiable for a driver's license in IL
#at least 16 years of age
#passed drivers exam
def drive_check():
    #collect our input
    age= int( input(" Please enter your age:"))  # init by defalt collects a string
    exam= input("Did you pass your exam( yes, no:)")
    #process the data with contionionals
    if age > 15 and exam == "yes": #it will evaluate it as TRUE or FALSE # 15 is an intiger and age is a string #two equal signs means it equal that
        print("You are eligiable to get your driver's licence") # it will do whatever is in the collans
    else: # is the opposite of if
        print("You are NOT eligible to get your driver's license")



# challenge 1
# 18 years of age or older
#U.S. citizen
def voteCheck():
    #collect you input
    age = int(input("Please enter your age:"))
    citizen = input("Are you a U.S. citizen(yes, no:)")
    if age > 18 and citizen == "yes" :
        print("You are ELIGIABLE to vote")
    else:
        print("You are NOT eligiable to vote")
    #process the data using contionals

#challenge 2
#a = int b= int c =int
#function prints the largest number out of a,b, and c
def max_num(a,b,c):
    # no input needed
    #figure out with is the largest, contional statements
    if a > b and  a > c:
        print("A is the largest number, the value of a is:" + str(a))
    if b > a and b > c:
        print(" B is the largest number, the value of b is:" + str(b))
    if c > a and c > b:
        print("C is the largest number, the value of c is:" + str(c))

#challenge 3
#Score = integer
#This function takes in a score and prints out the letter grade
def score_to_grade(score):
    #no input needed / scoreis our input
    #conditonals go her # atleast 5 if statements
    if score >= 90:
        print("A")
    elif score >=80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    elif score <= (59):
        print("F")


#notes
#boolean: true or false, type of data
#boolean:

#Compariso
# n Operatos ( add these ti notes)
#== equal to
# > greator than
# < less than
# >= greater than or equal to
#<= less than or euql to
#!= not equal to


#Logic Operators
# and Both statements must be TRUE
# or ONE of the statements must be TRUE
# not Return the opposite boolean


#main
score_to_grade(95)
