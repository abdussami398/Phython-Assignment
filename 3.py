# Assignment Qno#01
No1 = float(input('Enter a Number : '))
No2 = float(input('Enter  an other Number : '))
operator = input('Enter operation eg (-,+,/,*,**): ')

if (operator == '-'):
    result = No1 - No2
    print("Subtraction of ",No1," and ",No2," is ",result)
elif(operator == '+'):
    result = No1 + No2
    print("Addition of ",No1," and ",No2," is ",result)
elif(operator == '/'):
    result = No1/No2
    print("Division of ",No1," and ",No2," is ",result)
elif(operator == '*'):
    result = No1* No2
    print("Multiplication of ",No1," and ",No2," is ",result)
elif(operator == '**'):
    result = No1 ** No2
    print(No1," power ",No2," is: ",result)
else:
    print('Enter correct operator')




#Assignment Qno#02
List  = ["Hello", "World", 234, "Python", "Programming",False,30,0.331]

for i in List:
    if type(i) == int:
        print("Found numeric value: ",i)
        
        
        
#Assignment Qno#03 part A
Info = {'Name': 'Asad', 'Age': 23, 'Department': 'BSIT'}

print('''Before Update''')
print ("Info['Name']: ", Info['Name'])
print ("Info['Age']: ", Info['Age'])
print ("Info['Department']: ", Info['Department'])

print('''After Update''')

Info= {'Name': 'Asad', 'Age': 23, 'Department': 'BSIT'}
Info['Age'] = 30; # update existing entry
Info['School'] = "KBSAS Campus" # Add new entry

print ("Info['Name']: ", Info['Name'])
print ("Info['Age']: ", Info['Age'])
print ("Info['School']: ", Info['School'])




#Assignment Qno#03 part B
print('Before Update.')
data = {"Price1":291, "Price2":485,"Price3":645}  
print(data)

print("After Updating of Keys.")

data.update({"Price4":258}) #1st Method
data['Price5'] = 786  #2nd Method
print(data)


#Assignment Qno#4
def returnSum(dict): 
      
     sum = 0
     for i in dict.values(): 
           sum = sum + i 
       
     return sum
  
# Driver Function 
dict = {'a': 100, 'b':200, 'c':300} 
print("Sum :", returnSum(dict)) 


#Assignment Qno#5
def Repeat(x): 
    _size = len(x) 
    repeated = [] 
    for i in range(_size): 
        k = i + 1
        for j in range(k, _size): 
            if x[i] == x[j] and x[i] not in repeated: 
                repeated.append(x[i]) 
    return repeated 
  
# Driver Code 
list1 = [10, 20, 30, 20, 20, 30, 40,  
         50, -20, 60, 60, -20, -20] 
print (Repeat(list1)) 



#Assignment Qno#6
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present(5)
is_key_present(9)

