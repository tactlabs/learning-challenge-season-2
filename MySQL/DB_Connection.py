#Package to use MySQL
import mysql.connector



#Creating a connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Fanatic@7"
)
print(mydb)



#Crating a cursor to execute SQL statements
mycursor = mydb.cursor()



#Creating a Database
DB_Name = input("Enter the database name : ")
mycursor.execute("CREATE DATABASE {}" .format(DB_Name))

#Showing list of databases in your system
    #Method 1 -> To confirm database is created successfully
print("\nCheck whether database created by you is listed below")
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)
  
    #Method 2 -> To confirm database is created successfully
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Fanatic@7",
  #If Database creation is succcessful, No error shows up
  database=DB_Name
)
mycursor = mydb.cursor()
    


#Creating a table
print("A sample table has been created for you in {} database created by you" .format(DB_Name))
mycursor.execute("CREATE TABLE sample (name VARCHAR(255), Year VARCHAR(255))") 
#NOTE: Database has already been set in previous set while checking for its existence(Method 2)
print("\nCheck whether table created is listed below")
mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)






