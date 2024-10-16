# Polymorphism-meansPolymorphism in python is a term used to refer to an object's
# ability to take on multiple forms.
# to implement polymorphism we use duck typing.
# staic typing and dynamic typing
class Duck:
    def swim(self):
        print(" I am a duck and i can swim")
    def speak(self):
        print("Quack Quack")

class Dog:
    def swim(self):
        print(" I am a dog and i can swim")

    def speak(self):
        print("bhoo bhoo ")

class person:
    def speak(self):
        print("blah blah blaha")

def display(obj):
    obj.swim()
    obj.speak()
    print("information dispalyed")

d=Duck()        #create object of class duck
dog=Dog()       # craete obbject of class dog
p=person()

display(d)            # call method
display(dog)
display(p)             # it will not execute due to person object having no attribute swim

# it means python does not care about the class of the object if that method is defined on the object
# then it will call.Duck typing is a concept related to dynamic typing, where the type or the class of
# an object is less important than the methods it defines
#There are two types of polymorphism which are the compile-time polymorphism (overload) and run-time
# polymorphism (overriding)


