# hybrid inhertence- combination of two or more inheritence
class A:
    def display(self):
        print("disply from A class")
class B(A):
    def display(self):
        print("disply from B class")

class C:
    def show(self):
        print("hi from c class")
class D(B,A):
    def display(self):
        print("disply from D class")
d1=D()
d1.display()


