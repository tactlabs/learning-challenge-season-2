#A file named "Sample,txt" has been created initially

#Method 1-> To print every line one by one in the file(opened in read mode)
file = open('Sample.txt', 'r')
print("\n\nPrinting contents of Sample.txt using FOR loop")
for text in file: 
	print (text)
	
#Method 2-> To print every line one by one in the file(opened in read mode)
file = open('Sample.txt', 'r')
print("\n\nPrinting contents of Sample.txt using read() function")
print(file.read())

#Method 3-> To read() character wise(opened in read mode)
file = open("Sample.txt", "r")
print("\n\nPrinting first 7 characters from the contents of Sample.txt using read() function")
print(file.read(7))



#Create a file in write mode and writing something
File_Name = input("\n\nEnter file name(with '.txt' extension) : ")
File_Text = input("Enter content of file : ")
file = open('{}' .format(File_Name),'w') 
#write() is to write into a file
file.write("{}" .format(File_Text))
print("\nFile has been successfully created")
#Cross check whether new file is updated
print("CONTENT INSIDE NEWLY CREATED FILE IS")
file = open('{}' .format(File_Name),'r')
print(file.read())
file.close()



#To illustrate append() mode
Append_Text = input("\n\nEnter text to be appended to Sample.txt : ")
#'a+' -> append and read permission
file = open('Sample.txt','a')
file.write("{}" .format(Append_Text))
print("\nFile has been successfully created")
#Cross check whether new file is updated
print("AFTER APPENDING, CONTENT INSIDE Sample.txt FILE IS")
file = open('Sample.txt','r')
print(file.read())
file.close()



print("\n\n'With' keyword is used to automatically close a file")

	
