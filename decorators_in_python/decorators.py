'''''decorator is a function that takes another function as an argument
and returns a new function that modifies the behaviour of the original function

 '''''
def greet(hello):  #  here instead of hello u can use any name as a function inside that.
    def modified_fun():
        print("good morning")
        hello()
        print("by take care")
    return modified_fun



@greet   # here use greet decorator function
def hello():
    print("hello Amit")
hello()

# /////////////////////////////////////////////////////////////
print("///////////////////////////////////////////////////////////")
# ////////////////////////////////////////////////////////////////////
def greetuseargs(func):
    def modified_fun(*args,**kwargs):
        print("good morning")
        func(*args,**kwargs)
    return modified_fun


@greetuseargs
def add(a,b):
    print("addition is : ",(a+b))
add(5,6)

