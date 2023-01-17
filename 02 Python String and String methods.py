""" Here, we will demonstrate operations related to strings """


_strings = "Hello world"
print(_strings)




""" String Slicing  """
# String Slicing (Bascially cutting down the strings by index number)


print(_strings[5])                  #It will print value at index number 5
print(_strings[0:4])                #It will print values from index 0 to index 4
print(_strings[0:4:2])              #It will print values from index 0 to index 4 with the step of 2
print(_strings[:])                  #It will print all values from start to end
print(_strings[5:])                 #It will print values 5 to the END
print(_strings[-1:-7:-1])           #It will print values from -1(last value) to -7 in reverse steps


"""
__________________________________________________

__________________________________________________
"""

"""         String Methods      """





a = "I am the Prime Minister of The Republic of India "
print("length method")
print(len(a))                       #To find the length of the strings



print("count method ")
print(a.count('i'))                 #Counts how many times a specific value occurs


print("upper()  method  ")
print(a.upper())                    #converts to upper case
print(a.isupper())                  #check whether it is the upper case or not

print("lower()   method")
print(a.lower())                    #converts to lower case
print(a.islower())                  #check whether it is the lower case or not


print("find()    method")
print(a.find("i")) #Find the first index where i char occurs



print("replace() method")
print(a.replace("India","Korea"))   #It finds the character and replace it
