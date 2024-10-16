class A:
    def display(self):
        print("disply from A class")
class B(A):

    def display(self):
        print("disply from B class")

class C(A):
    def show(self):
        print("hi from c class")
    # def display(self):
    #     print("disply from C class")

class D(B,C):
    pass
    # def display(self):
    #     print("disply from D class")

d1=D()
d1.display()
print(D.mro())   # when u run it will check first D class method of display not exist any go for B then c
                # in left to right then above class then super class finally check,