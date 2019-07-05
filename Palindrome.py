#Function which return reverse of a string 
def Reverse(s):
    #Syntax-> [Start:End:Step]
        #'-1' means in reverse order
    return s[::-1] 


def isPalindrome(s): 
	# Calling reverse function 
	rev_text = Reverse(s) 

	# Checking if both string are equal or not 
	if (s == rev_text): 
		return True
	return False


# Driver code 
text = input("Enter the string to check whether it is a palindrome or not : ")
text = text.upper()
ans = isPalindrome(text) 

if ans == 1: 
	print("\nYes, {} is a palindrome" .format(text)) 
else: 
	print("\nNo, {} is not a palindrome" .format(text)) 
