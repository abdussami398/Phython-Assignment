#Assignment Qno#1
a ="Twinkle, twinkle, little star,\n"
b ="\tHow I wonder what you are!\n"
c = "\t\tUp above the world so high,\n"
d ="\t\tLike a diamond in the sky.\n"

print(a+b+c+d+a+b);


#Assignment Qno@2
import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)


#Assignment Qno#3
import datetime    # this is a packege which helps you run/ show the recent Date and Time.
show = datetime.datetime.now()
print("The Current Time Is: %s:%s:%s" %(show.hour, show.minute,show.second))
print("The Current Day Is: %s/%s/%s" %(show.day, show.month,show.year))



#Assignment Qno#4
R = int(input("Please Enter the value of Radius to get the Area: "))
Area = 3.14*(R**2)
print("The Area of cirlce in meters is: ",Area)


#Assignment Qno#5
F = input("Enter First Name Please: ")
L = input("Now Enter Last Name: ")
N = L+" "+F
print(N)



# Assignment Qno#6 
x = int(input("Please Enter a Number: "))
y = int(input("Now Enter another number: "))
z = int(x+y) #Addition
print("The Addition of ",x," and ",y, "is: ",z)