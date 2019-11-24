#Qno 1
    #Marksheet to get Grade:
Cplus = int(input("Enter C++ Marks: "))
Java = int(input("Enter Java Marks: "))
Python = int(input("Enter Python Marks: "))
OOP = int(input("Enter OOP Marks: "))
C = int(input("Enter C Language Marks: "))
TOb = Cplus + Java + Python + OOP+C
Total = 500
print("Total obtained marks ",TOb," out of ",Total)
per = TOb/Total*100
print("your %",per)
if per > 100:
        print("Invalid %")
elif per >= 80 and per <= 100:
        print("Your Grade is 'A'.")
elif per >= 60 and per <= 79:
        print("Your Grade is 'B'.")
elif per >= 50 and per <= 59:
        print("Your Grade is 'C'.")
elif per >= 40 and per <= 49:
        print("Your Grade is 'D'.") 
else:
        print("You are Fail.")




# Qno 2
    #Get Even Odd
No1 = int(input("Enter A Number: "))
if No1%2 ==0:
        print("The Number is Even")
else:
        print("The Number is Odd")



# Qno 3
    #Length of  Array
Arr = ("asad","Nsaeer",12,0.43,'A',False)
print("The Length of Given Array is: ",len(Arr))


# Qno 4
    #Largest number in Array
Arr = (12,0.43,False,12.001,11.99)
print("The Largest value in Given Array is: ",max(Arr))



# Qno 5
    #Sum of List
Arr = [34,.034,97.09,45]
print("The Sum of all elements in the given list: ",sum(Arr))



# Qno 6
    #Less than 5
Arr = [1,1,2,3,4,5,6,7,8,0]
print("Elements less than 5 are: ",Arr[:5])
