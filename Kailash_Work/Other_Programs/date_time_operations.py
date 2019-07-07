#INCLUDE statements for using date and time attributes
import datetime
present = datetime.date.today()
print("Today's data is {}" .format(present)) #prints the today's date completely

#print different attributes of the date
print("Day is {}".format(present.day))
print("Month is {}".format(present.month))
print("Year is {}".format(present.year))

#print date in different format
print("\nPrinting date in different format")
print(present.strftime("%d %B,%Y (%A)"))
print(present.strftime("please attend our event on %A,%B %d in the year %Y"))

#d,b,y,B,Y,a,A
#date,month,year(2 dig),month(Full),year(4 dig),day,day(Full)

#To find difference between the dates
birthstr = input("\nEnter your upcoming birthdate in dd/mm/yyyy format:")#specify the date format to eliminate errors
print(birthstr)
#Converting string type to datetime type (by default input will be of string type)
    #date() at the end is used, since we need only no of days and not time
birthdate = datetime.datetime.strptime(birthstr,'%d/%m/%Y').date() 
diff = birthdate - present
print("You have still {} days left for your birthday" .format(diff.days)) #since we need only no of days and not time

#To dispaly Calendar
    #Package needed to work with Calendars
import calendar  
# Enter the month and year
print("\nCALENDAR DISPLAY")
year = int(input("Enter year: "))  
month = int(input("Enter month: "))  
  
# display the calendar
print("\n")
print(calendar.month(year,month))

#-------------------------------------------------------------------------------

#already datetime has been imported

timesnow = datetime.datetime.now()
print("\nCuurent Time is {}" .format(timesnow))

#print different attributes of time
print("Hour shows {}" .format(timesnow.hour))
print("Minute shows {}" .format(timesnow.minute))
print("Second shows {}" .format(timesnow.second))

#print time in different format
print("\nPrinting time in different format")
print(datetime.datetime.strftime(timesnow,"%H:%M:%S %p")) #p is for denoting pm or am
