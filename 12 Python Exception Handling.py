# Exception handling

# Catching errors with 
# with try and except statements

try:
    age = int(input("Age: "))
    income = 200
    risk = income/age
    print(age)

except ZeroDivisionError:
    print("Age Can't be zero")

except ValueError:
    print("Invalid Value")
    






 
# Raising an Exception in Python  
num = [3, 4, 5, 7]  
if len(num) > 3:  
    raise Exception( f"Length of the given list must be less than or equal to 3 but is {len(num)}" )  










# The assert statement

 
# defining a function  
def square_root( Number ):  
    assert ( Number < 0), "Give a positive integer"  
    return Number**(1/2)  
  
#Calling function and passing the values  
print( square_root( 36 ) )  
print( square_root( -36 ) )  









# Try with Else Clause
 
# Defining a function which returns reciprocal of a number  

def reciprocal( num1 ):  
    try:  
        reci = 1 / num1  
    except ZeroDivisionError:  
        print( "We cannot divide by zero" )  
    else:  
        print ( reci ) 
         
# Calling the function and passing values  
reciprocal( 4 )  
reciprocal( 0 )  









# Finally Keyword in Python
# Raising an exception in try block  
try:  
    div = 4 // 0    
    print( div )  
# this block will handle the exception raised  
except ZeroDivisionError:  
    print( "Atepting to divide by zero" )  
# this will always be executed no matter exception is raised or not  
finally:  
    print( 'This is code of finally clause' )  