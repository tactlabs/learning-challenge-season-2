#Package to use MySQL
import mysql.connector


#Creating a connection and opening the specified DB
DB_Name = input("Enter the database name : ")
mydb = mysql.connector.connect(
  host="localhost",
  user="# Your username #",
  passwd="# Your password #",
  database=DB_Name
)


#Crating a cursor to execute SQL statements
mycursor = mydb.cursor()


#Getting inputs from user
Table_Name = input("\n\nEnter table name in {} DB to insert values : " .format(DB_Name))
Name = input("Enter Student Name : ")
Department = input("Enter Department : ")
#SQL query to insert into table
sql = "INSERT INTO {} VALUES (%s , %s)" .format(Table_Name)
val = ("{}" .format(Name) , "{}" .format(Department))
mycursor.execute(sql, val)
#To save changes
mydb.commit()
print("\n")
print(mycursor.rowcount, "record inserted.")


#Cross check whether record is inserted
mycursor.execute("SELECT * FROM {}" .format(Table_Name))
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
