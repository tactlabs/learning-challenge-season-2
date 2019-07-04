#Creating and initializing a string variable
g="Hello, Greetings to everyone gathered"
print("Sentence used for explaining basic String operations is")
print(g)


#Finding length of string
print("\n\nLength of the string is")
print(len(g))


#To crop a secton of string and print
print("\n\nCropping the word 'everyone' from the string by specifying index range")
    #NOTE:Range will consider only till "ENDPOINT-1" element
print(g[20:28])


#Printing the string in uppercase
print("\n\nUppercase of given string")
print(g.upper())


#Printing the string in lowercase
print("\n\nLowercase of given string")
print(g.lower())


#Returning the starting index of a word in the string
print("\n\nStarting index of word 'Hello' in the string is")
print(g.find("Hello"))


#Replacing words
g=g.replace("Hello" , "hi")
print("\n\nReplacing the word 'Hello' by 'Hi' in the string")
print(g)


#Counting the occurences
print("\n\nNumber of occurences of the letter 'e' in the string is")
print(g.count('e'))


#capitalizes first letter
print("\n\nAfter capitalizing first letter of the string")
print(g.capitalize())


#splitting based on spaces
g=g.split(' ') 
print("\n\nSplitting string with SPACE as the delimiter")
print(g)

