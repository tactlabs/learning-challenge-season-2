#Defining a class "Student" to hold details about a student
class Student:
    #Constructor
        #Initilaizing parameters recieved to local variables
    def __init__(self, name, dept, year):
        self.name = name
        self.dept = dept
        self.year = year


#Creating objects of class Student
print("\nStatic Objects created")
    #Object 1
SK7 = Student("SK7", "CSE", "4th")
#Displaying object information
print("\nEntries held by Object 1 are : ")
print(SK7.name)
print(SK7.dept)
print(SK7.year)

    #Object 2
Kailash = Student("Kailash", "ECE", "3rd")
#Displaying object information
print("\nEntries held by Object 2 are : ")
print(Kailash.name)
print(Kailash.dept)
print(Kailash.year)






