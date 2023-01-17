# Dictionary is another type of collection in Python
# it stores elemetnts in " Key = value " pair .

dict ={
   "name": "Hii",
   "list":{
       "first": "One",
       "second": "Two",
       "third": "Three",
   },
   "list2":[8,7,6,5,4],
   }
print("Dictionary demonstration")   
print(dict["list"]["first"])
print(dict["list2"][2])

# This example convert entered phone numbers
# into their spellings

phone =input("Phone: ")

digit_map={

    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}

am =""
for Char in phone:
    am += digit_map.get(Char,"!") +" "
print(am)