# Method overloading--is we are defining many methods with same name but diffrent arguments or
# parametres in a same class   but in python it not supported it also called compile time polymorphism.

# class Demo:
#     def add(self,a,b):
#         return a+b
#
# d=Demo()
# print(d.add(4,5))  # output =9 it work

#------------------------------------------------------
# class Demo:
#     def add(self,a,b):
#         return a+b
#     def add(self,a,b,c):
#         return a+b+c
#
# d=Demo()
# print(d.add(4,5))
# print(d.add(4,5,6))               # it will give error of missing positional argument.

#------------------------------------------------------------------------------
class Demo:
    def add(self,a,b,c=0):  # here we use deafault argument by achive method overloading.
        return a+b+c


d=Demo()
print(d.add(4,5))
print(d.add(4,5,6))

# it gives output proper 9 15
#------------------------------------------------------------------------------

class Demo:
    def add(self,*args):  # for varible length arguments we use *args
        total=0
        for i in args:
            total=total+i
        return total

d=Demo()
print(d.add(4,5))
print(d.add(4,5,6))
print(d.add(4,5,6,5,6,7,8,9,4,5))