#Function to perform Selection sort
def sort_fun(a) :
    i=0
    temp = 0
    #Logic for performing selection sort
    for i in range(len(a)) :
        min = i
        for j in range(i+1,len(a)) :
            #Comparing 2 successive elements until end of the list
            if(a[j] < a[min]) :
                min = j
        #Swapping the numbers
        temp = a[i]
        a[i] = a[min]
        a[min] = temp
    #Returning sorted list
    return a

                
            
            
