#jocelyn Garcia
#10/23/2024
#variable swap


#swap the value of x and y with out using any numbre using 3 lines or less

x=10
y=4
z=0

#your code goes here...
z=x # z hold on to the 10
x=y#then change x to  the y value
y=z # then y equals z
#z is holding the value of x


print(str(x))#should print 4
print(str(y)) #should print 10


#jocelyn garcia
#11/20/2024

x = 0 # global variables
y = 0 #global variables
# global variables cna be used anywhere

def test():
    global x
    global y
    x = 10 #local
    y = 5 #local


test()
print(x)
print(y)
