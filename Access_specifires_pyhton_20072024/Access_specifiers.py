# Access specifiers in python public,protected,private: is used to set the limit of member accesibilty.

# class student:
#     def __init__(self,name):
#         self.name=name
#     def display(self):
#         print(f"hi my name is {self.name} from student class")
#
# stude1=student("amit")
# print(stude1.name)
# stude1.display()

# class A:
#     a=100 #public
#     _b=200 #protected
#     __c=None #private
#
#     print(a," ",_b," ",__c)

class A1:
    a=100
    _b=200
    __c=None
    print(a, " ",_b," ",__c)
    def __add(self):
        self.__c=self.a+self._b
        print("Addition=",+self.__c)

        # print(self.__c)  here u can call this private variable inside the same class


obje=A1()
obje._A1__add()
print(obje._A1__c)   # when u want to call outside the class private variable then use (obj._classname__variblename)
                        # is called mengling.
