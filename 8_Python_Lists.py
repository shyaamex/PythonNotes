# List is nothing but  a sequence data type similar to 
# array, which is used to store multiple values in a single
# vailable

list=[1,2,3,4,5]
print(list)
# You can LOOP through the list
# Find the largest number in the list

list = [1, 2, 3, 6, 11, 3, 44]
Largest =list[0]
for items in list:
    if Largest <items:
        Largest = items
print(Largest)


# Similar to the strings in python, you can slice the list as well

print(list[3])
print(list[-1])
print(list[2:])



# 2D lists
matrix =[
    [1,2,3],
    [4,5,6],  
    [7,8,9]]

print(matrix[0][1])
print(matrix[1][1])

        





# List Methods in Python

a = [1,2,3,4,5,6,7,8]
a.append(1)             # Append method adds a value at the end of the lists
print(a)


a.clear()               #Makes the list empty
print(a)

b=[12,23,34,45]
c=b.copy()              # Creates a copy of the list
print(c)



b.insert(2,46)          # Insert an element at the specified positions
print(b)



print(b.extend(c))      # Add a list at the end of another list



b.pop()                 # Remove the last value from the list
print(b)


# Unpacking Python lists

coordinates = [1,2,3]

x , y, z = coordinates

print(z)
print(x)