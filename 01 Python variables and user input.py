""" 
In python we don't need to assign datatype to any variable, Python interpreter automatically
assign datatype to the variables as per the given in input

"""


a=10                #integer
b=10.11             #float
c=a+3j              #complex number
shyam="Shyam"       # String

print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))
print(shyam)
print(type(shyam))

""" How to accept values from users? """
user = input("Please, enter your name!!")
print("hii, " + user)







# Input function by default takes input as string although 
# we can typecast them

age = input("Enter your age : ")            # Entered values would be of string class
print(type(age))                            

age_int=int(input("Enter your age : "))     # Entered values would be converted to int class 
print(type(age_int))

print(age)

