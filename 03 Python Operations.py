"""         Operators in Python             """

#   Arithmatic Operators
print("Arithmatic Operators")
print(5+2)
print(5-2)
print(5/2)          # Returns Floating point.
print(5//2)         # Returns Integer.
print(5%2)          # Returns Remainder
print(5*2)
print(5 ** 2 )      # Power to 3


print("Assginment Operators")
#   Assigment Operators
x = 5
print(x)
x+=5            # Adds 5 to x and assign back to x
print(x)        
x-=3            # Subtracts 3 to x and assign back to x
print(x)
x *= 3          # Multiplies 3 to x and assign back to x
print(x)
x /= 3          # Divides x to 3 and assign back to x
print(x)

print("Comparison Operators ")
a=5
b=8
print(a==b)         # Compare whether "a" is EQUAL to "b" or not
print(a>=b)         # Compare whether "a" is GREATER THAN or EQUAL to "b" or not
print(a<=b)         # Compare whether "a" is LESS THAN or EQUAL to "b" or not
print(a>b)          # Compare whether "a" is GREATER THAN "b" or not
print(a<b)          # Compare whether "a" is EQUAL to "b" or not
print(a!=b)         # Compare whether "a" is EQUAL to "b" or not





print("Logical Operator ")


print(a>b and a<b)          #Returns True if both statements are true
print(a>b or a<b)           #Returns True if one of the statements is true
print(not(a>b and a<b))     #Reverse the result, returns False if the result is true


print("Identity Operators")


a=[4,5,6]
b=[4,5,6]
c=a
print(a is b)               # returns False because "a" is not the same object as "b", even if they have the same content
print(a is c)               # returns True because "a" is the same object as "b"






print("membership operators")
a=[1,2,3,4,5]


print(1 in a)           # Check the mebership
print(1 not in a)

