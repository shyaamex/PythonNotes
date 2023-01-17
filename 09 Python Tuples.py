# Tuples are sequence datatype similar to lists, but they are " immutable "


tup =(1,2,3,4)

print(tup[0])
tup.count
tup.index(2)

# All opetaions performed on the lists can be performed on tuples, 
# but you can't alter the values and size of tuple



# You can LOOP through the list
# Find the largest number in the list

_tuple = (1, 2, 3, 6, 11, 3)
Largest =_tuple[0]
for items in _tuple:
    if Largest <items:
        Largest = items
print(Largest)



print(_tuple[-1::-1])
print(_tuple[2::2])


# if you want to add a value in tupel 
# You need to change it into list, alter and
# then covert back to tuple.
print(f"Tuple before : {_tuple} ")
a=list(_tuple)
a.append(35)
_tuple=tuple(a)
print(f"Tuple after  : { _tuple } ")