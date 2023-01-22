# Inheritance in python

class first:
    pass #Pass means nothing




class Mammal:
    def walk(self):
        print("Walk")

class Dog(Mammal):

    def bark(self):
        print("Bark!!")

    

dog = Dog()
dog.walk()
dog.bark()


