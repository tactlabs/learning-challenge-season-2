#Declaring a list
a = [1,2,3,4,5]
print("List is {}" .format(a))

#adds item at the last
a.append(6)
print("\nAfter appending '6' to the list")
print(a)

#removes last element
a.pop()
print("\nAfter popping out last element")
print(a)

#removes that particular element
a.remove(5)
print("\nAfter removing '5' from the list")
print(a)

#deletes the element in that position
del a[0]
print("\nAfter removing element at index '0'")
print(a)

#Overwriting element in a particular index of the list
a[0] = 0
print("\nOverwriting element at index 0")
print(a)




#Declaring a list
b = [1,2,3,4,5,6]
print("\n\n\n\nList is {}" .format(b))

#returns the index of specified element
print("\nIndex of item '6' is {}" .format(b.index(6)))

#Printing list members one after the other
print("\nMembers of the List 'a' is")
for i in range(len(b)) :
    print(b[i])
    



#Creating a list
c = ['a','c','b','e','d']
print("\n\n\n\nList is {}" .format(c))

#Sorting the list alphabetically
c.sort()
print("\nAfter sorting the list alphabetically")
print(c)


    

