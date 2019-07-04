#Creating a Dictionary
SK7dict = {
  "Name": "Kailash S",
  "DOB": 1998,
  "Interest": "Machine Learning"
}
print("Dictionary created is SK7dict {}" .format(SK7dict))
#To find length of dictionary
print("Size of the dictionary is {}" .format(len(SK7dict)))



#Accessing an item from dictionary
    #Method 1
x = SK7dict.get("Name")
print("\n\nName of the student in the SK7dict dictionary is {}" .format(x))
    #Method 2
y = SK7dict["Interest"]
print("Interest of the student in the SK7dict dictionary is {}" .format(y))



#To change value of one of the keys in dictionary
SK7dict["Interest"] = "Artificial Intelligence"
print("\n\nAfter modifiyng values of a key")
print("SK7dict Dictionary is {}" .format(SK7dict))



#Displaying Dictionary
    #To display only KEYS
print("\n\nKEYS in SK7dict dictionary are : ")
for key in SK7dict :
    print(key)
    
    #To display only VALUES
print("\nVALUES in SK7dict dictionary are : ")
for key in SK7dict :
    print(SK7dict[key])

    #To display both KEYS and VALUES
print("\nBoth KEYS and VALUES in SK7dict dictionary are : ")
for key , value in SK7dict.items() :
    print(key , value)



#To check whether a key is there in the dictionary
key_check = input("\n\nEnter the key to check its availability in the SK7dict dictionary : ")
key_check = key_check.capitalize()
if key_check in SK7dict :
    print("Yes, {} key is there in SK7dict dictionary" .format(key_check))
else :
    print("No, {} key is not there in SK7dict dictionary" .format(key_check))



#Adding items to dictionary
input_key = input("\n\nEnter key to be added : ")
input_value = input("Enter correspinding value yo be added : ")
SK7dict[input_key] = input_value
print("SK7dict dictionary after adding new item is {}" .format(SK7dict))


#To delete an item from dictionary
del_key = input("\n\nEnter the key to be deleted : ")
del_key = del_key.capitalize()
del SK7dict[del_key]
print("\n\nAfter deleting {} key from SK7dict dictionary {}" .format(del_key , SK7dict))



#To copy a dictionary
SK7dict2 = SK7dict.copy()
print("\n\nCopy of Sk7dict : SK7dict2")
print(SK7dict2)




    




