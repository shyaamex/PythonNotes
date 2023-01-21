# Python Constructor


# A constructor is a special type of method (function) which is 
# used to initialize the instance members of the class.


# In Python, the method the __init__() simulates the constructor of the class.

# It accepts the self-keyword as a first argument which allows accessing the attributes or method of the class.





class Employee:  
    # constructor
    
    def __init__(self, name, id):  
        self.id = id  
        self.name = name  
  
    def display(self):  
        print(f"ID: {self.id} \n Name: {self.name} " ) 
        
# Creating objects
emp1 = Employee("John", 101)  
emp2 = Employee("David", 102)  
  
# accessing display() method to print employee 1 information  
  
emp1.display()  
  
# accessing display() method to print employee 2 information  
emp2.display()       
        
