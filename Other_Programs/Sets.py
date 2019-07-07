#Sets remove duplicates
Text = input("Enter a statement(with some redundant words of same case)")
    #Splitting the statement into individual words and removing redundant words
Text = (set(Text.split()))
print(Text)


#Creating 2 sets
print("\nCreating 2 sets")
a = set(["Jake", "John", "Eric"])
print("Set 1 is {}" .format(a))
b = set(["John", "Jill"])
print("Set 2 is {}" .format(b))


#Adding elements
print("\nAdding 'SK7' item to both sets")
a.add("SK7")
b.add("SK7")
print("Set 1 after adding 'SK7' : ")
print(a)
print("Set 2 after adding 'SK7' : ")
print(b)


#Removing elements
del_index = (input("\nEnter the element to be removed in set 1: "))
a.remove(del_index)
print("After removing specified element")
print(a)


#Finding intersection
print("\nIntersection between set 1 and set 2 gives : ")
print(a.intersection(b))


#Finding items present in only one of the sets
print("\nItems present in only one of the 2 sets : ")
print(a.symmetric_difference(b))
print("\nItems present only in set a : ")
print(a.difference(b))
print("\nItems present only in set b : ")
print(b.difference(a))


#Finding union of 2 sets
print("\nUnion of 2 sets : ")
print(a.union(b))


#Clearing sets
print("\nClearing sets 1 and 2")
print("Set 1 is {}" .format(a.clear()))
print("Set 2 is {}" .format(b.clear()))

