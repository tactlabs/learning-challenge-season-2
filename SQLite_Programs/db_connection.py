#Importing sqlite3 package
import sqlite3
#Connection object that represents the database "schooltest.db"
MySchool=sqlite3.connect('schooltest.db')
#Creating cursor objects to perform basic SQL operations
curschool=MySchool.cursor()


#Executing "CREATE TABLE" SQL operation
    #StudentID is set as the primary key
    #AUTOINCREMENT"-> ID's will automatically created for each entry by incrementing '1'
    #NOT NULL-> Making it a "required" variable
curschool.execute('''CREATE TABLE IF NOT EXISTS student (
StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT (20) NOT NULL,
age INTEGER,
marks INTEGER);''')
#Commit to the database
MySchool.commit()


#Inserting one static data into the database
    #While running this program for second time comment out this piece of code as UNIQUE constraint fails for StudentID 
curschool.execute('''INSERT INTO student
VALUES (70,'Kailash',20,50);''')
#Commit to the database
MySchool.commit()


#Inserting one dynamic data by getting input from user
mID=int(input("Enter ID : "))
mname=input("Enter name : ")
mage=int(input("Enter age : "))
mmarks=int(input("Enter marks : "))
curschool.execute('''INSERT INTO student
VALUES(?,?,?,?);''',(mID,mname,mage,mmarks))
#Commit to the database
MySchool.commit()


#Displaying records from database
sql="select * from student"
curschool.execute(sql)
print("\n\nDisplaying all records in the database")
while True:
    #Retrieves rows one after another
    record=curschool.fetchone()
    #If the record is NULL
    if record==None:
        break
    print (record)


#Displaying records matching a condition
nm=input("\n\nEnter name of the student to display his/her records : ")
sql="SELECT * from student WHERE name='"+nm+"';"
curschool.execute(sql)
record=curschool.fetchone()
print(record)


#Updating field of a record matching a condition
nm=input("\n\nEnter name of the student to modify his/her marks : ")
sql="SELECT * from student WHERE name='"+nm+"';"
m=float(input("enter new marks : "))
sql="UPDATE student SET marks='"+str(m)+"' WHERE name='"+nm+"';"
try:
    curschool.execute(sql)
    #Saving the changes
    MySchool.commit()
    print ("record updated successfully")
except:
    print ("error in update operation")
    MySchool.rollback()

#Final commit to the database
MySchool.commit()
#Closing the connection
MySchool.close() 
