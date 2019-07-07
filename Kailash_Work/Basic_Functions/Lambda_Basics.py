#A lambda function that multiplies argument a with argument b
print("Enter 2 inputs to be multiplied : ")
In1 = int(input("Enter number 1 : "))
In2 = int(input("Enter number 2 : "))
x = lambda a, b : a * b
prod = x(In1, In2)
print("Product of {} and {} is {}" .format(In1, In2, prod))




#A lambda function that sums argument a, b, and c
print("\nEnter 3 inputs to be added : ")
In1 = int(input("Enter number 1 : "))
In2 = int(input("Enter number 2 : "))
In3 = int(input("Enter number 3 : "))
x = lambda a, b, c : a + b + c
add = x(In1, In2, In3)
print("Sum of {},  {} and {} is {}" .format(In1, In2, In3, add))



#Lambda function defined inside another function
def myfunc(n):
  return lambda a : a * n

#Creating a function that always doubles the number
    #Assigning the function containing lambda to a variable with '2' as parameter(doubles the number)
In1 = int(input("\nEnter the number to find its doubler : "))
mydoubler = myfunc(2)
#Calling the "mydoubler" function
doubler = mydoubler(In1)
    #2->'n' ; In1->a
print("Doubler of {} is {}" .format(In1, doubler))

#Creating a function that always triples the number
    #Assigning the function containing lambda to a variable with '3' as parameter(doubles the number)
In1 = int(input("\nEnter the number to find its tripler : "))
mytripler = myfunc(3)
#Calling the "mydoubler: function
tripler = mytripler(In1)
    #3->'n' ; In1->a
print("Tripler of {} is {}" .format(In1, tripler))
