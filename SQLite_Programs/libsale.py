#Importing sqlite3 package
import sqlite3
#Connection object that represents the database "library.db"
MyLib=sqlite3.connect('library.db')
#Creating cursor objects to perform basic SQL operations
curlib=MyLib.cursor()


#Calculating the cost for book purchase by fetching cost from database
print("Details for calculating cost for the book(s)")
mname=input("\nEnter name : ")
quantity=int(input("Enter no of copies : "))
#Taking the record matching the name of the book entered by the user"
sql="select price from books WHERE title='"+mname+"';"
curlib.execute(sql)
tprice=curlib.fetchone()
#Fetching the price of the book (INDEX 0) from the record
price=int(tprice[0])
#Calculating total cost
total=price*quantity
print("Total price is {}" .format(total))

