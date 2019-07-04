#Creating an empty list and a placeholder to store string
entry = []
people = " "


print("Enter the names of people and type 'done' if all inputs have been given%")
#Getting first input from user and changing first letter to upper case
people = input("\nEnter the Name : ").capitalize()
#Appending it to the list (if input is not "DONE")
if(people != "Done"):
    entry.append(people)
    

#Getting input(s) from user and changing first letter to upper case (until user types "DONE" as input)
while(people != "Done") :
    people = input("Enter the Name: ").capitalize()
    if(people != "Done") :
        #Appending it to the list (if input is not "DONE")
        entry.append(people)
        

#Sorting the list alphabetically        
entry.sort()
#Printing the sorted list
print("\n\nSorted list is")
for i in entry :
    print(i)
