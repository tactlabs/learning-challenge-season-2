#Function for finding factorial is defined
    #Function is named as "factorial" and returns the factorial of a number
    #Function accepts one integer parameter for which factorial is to be found
def factorial(number):
    #Variable is initialized to "one" as we are going to multiply inside "for" loop
    fact = 1
    #Logic to find factorial
    for i in range(number):
        fact = fact * (i+1)
    return fact

