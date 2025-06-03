#Jocelyn Garcia
#01/23/2025
#list practice



#Initialize
#mySchedule stores a list of the classes you are currently taking at Jones  as strings
#Initialize the list with your first three periods ONLY
mySchedule = []

#Main

#Complete the following tasks using list/array methods. Print the result for each task.

#Task 1: Append periods 4 - 7 to the list
mySchedule = ["English", "Biology", "APGOV"]
mySchedule.append("Math") # adds class to the list  # task 1
mySchedule.append("APCSP")  # task 1
mySchedule.append("PE")  # task 1
mySchedule.append("APspanish") # task 1
print(mySchedule)

#Task 2: Insert your two lunch periods(A day and B Day) in their appropriate location
mySchedule = ["English", "Biology", "APGOV"]
mySchedule.append("Math") # adds class to the list  # task 1
mySchedule.append("APCSP")  # task 1
mySchedule.append("PE")  # task 1
mySchedule.append("APspanish") # task 1
mySchedule.insert(3,"B lunch") # adds lunch in a specific place
mySchedule.insert(8,"C lunch")
print(mySchedule)

#Task 3: Remove your least favorite class
mySchedule = ["English", "Biology", "APGOV"]
mySchedule.append("Math") # adds class to the list  # task 1
mySchedule.append("APCSP")  # task 1
mySchedule.append("PE")  # task 1
mySchedule.append("APspanish") # task 1
mySchedule.insert(3,"B lunch") # adds lunch in a specific place
mySchedule.insert(8,"C lunch")
mySchedule.pop(1) # removed the class (Biology class) task 3
print(mySchedule)


#Task 4: Print just your 2nd period class by accessing the appropriate index in your array
mySchedule = ["English", "Biology", "APGOV"]
mySchedule.append("Math") # adds class to the list  # task 1
mySchedule.append("APCSP")  # task 1
mySchedule.append("PE")  # task 1
mySchedule.append("APspanish") # task 1
mySchedule.insert(3,"B lunch") # adds lunch in a specific place
mySchedule.insert(8,"C lunch")
print(mySchedule)
print(mySchedule[7]) # prints specific class

#Task 5: Print only your A day schedule and then only your B day schedule
print(mySchedule[0:5]) # print my A day
print(mySchedule[5:9]) # prints my b day
