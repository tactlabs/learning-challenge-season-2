#Importing factorial.py as module to find factorial
    #Renaming factorial module as fact
import factorial as fact

#Importing fibonacci.py as module to find fibonacci series
    #Renaming fibonacci module as fib
import fibonacci as fib


fact_inp = input("\nEnter the number to find its factorial : ")
#By default input is of String type in python
fact_inp = int(fact_inp)
print(fact.factorial(fact_inp))

fib_inp = input("\nEnter the last index of the required fibonacci series : ")
#By default input is of String type in python
fib_inp = int(fib_inp)
print(fib.fibonacci(fib_inp))
