#This function adds two numbers 
def add(x , y):
   return x + y

#This function subtracts two numbers 
def sub(x , y):
   return x - y

#This function multiplies two numbers
def mul(x , y):
   return x * y

#This function divides two numbers
def div(x , y):
   return x / y


#Flag variable used for calculator termination purpose
    #Initially flag is set to 0
flag = 0

#Until the user chooses option 5(Stop), calculator keeps on working
while(flag == 0):
    #Choices displayed
    print("\n\n\nSelect operation")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Stop")
    
    #Take input from the user 
    choice = input("\nEnter choice : ")
    if(choice == '5'):
        #If user wishes to stop calculator(choice 5), flag is set to 1
        flag = 1
    #If user has chosen choice 5(stop), control comes out of loop here, failing to satisfy the condition
    if(flag == 0):
        num1 = int(input("\nEnter first input : "))
        num2 = int(input("Enter second input : "))

        #Performing corresponding arithmetic operation
        if choice == '1':
           print("\nSum of {} and {} is {}" .format(num1 , num2 , add(num1,num2)))
        elif choice == '2':
           print("\nDifference between {} and {} is {}" .format(num1 , num2 , sub(num1,num2)))
        elif choice == '3':
           print("\nProduct of {} and {} is {}" .format(num1 , num2 , mul(num1,num2)))
        elif choice == '4':
           print("\nDivision of {} and {} is {}" .format(num1 , num2 , div(num1,num2)))
        else:
           print("Invalid operation")

#Comes out of the loop, if user chooses choice 5(flag is set to '1')
print("\nCalculator service terminated")
