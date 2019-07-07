#Creating a class "product"
class product:
    
    #Creating a variable to assign deliveryCharge
    #This belongs to the "product" class and common to all instances
    deliveryCharge=50
    
    #Constructor
        #If parameter values(nam, prc) are not mentioned, default values will be taken
        #'self' helps to access attributes and methods of class for that particular instance
        #NOTE: Constructor parameters should be used through 'self' only
    def __init__(self,nam="Teddy Bear", prc=500):
        #Assigning name and price of object to new variables
        self.name=nam
        self.price=prc
        
    #Function to get name of the product
    def get_name(self):
        return self.name
        
    #Function to compute total cost
    def get_price(self):
        return self.price + product.deliveryCharge

    #Function to print the cost summary
    def show(self):
        print("Name of the product ordered is {}" .format(self.name))
        print("The {} without wrapping charges will cost you Rs.{}.".format(self.get_name(),self.get_price()))





#Creating another class "gift" inherited from "product"
class gift(product):

    #Creating a variable to assign WrappingCharge
    #This belongs to the "gift" class and common to all instances
    Wrappingcharge=100

    #Constructor of "gift" class inturn calls constructor of "product" class
    def __init__(self,nam="Teddy Bear", prc=500):
        super().__init__(nam,prc)

    #Function to compute total cost(including wrapping)
    def get_price(self):
        return self.price + product.deliveryCharge + gift.Wrappingcharge

    #Function to print the cost summary
    def show(self):
        print("Name of the product ordered is {}" .format(self.name))
        print("The {} with wrapping charges will cost you Rs.{}.".format(self.get_name(),self.get_price()))
    
    
    
