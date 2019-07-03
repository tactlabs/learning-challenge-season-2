#Function for finding fibonacci series of 'n' terms is defined
    #Function is named as "fibonacci" and returns the fibonacci series of a number
    #Function accepts one integer parameter for which fibonacci series is to be found
def fibonacci(n) :
    #First 2 terms of any fibonacci series by default is '0' and '1'
    terms = [0,1]
    #Start finding out the elements from index '2'
    i=2
    #Logic to find fibonacci series
    while(i<=n) :
        terms.append(terms[i-1] + terms[i-2])
        i=i+1
    #If n is '0', you should return only '0'
    if(n == 0) :
        terms = [0]
    #Returns the fibonacci series of 'n' terms as a list
    return terms
