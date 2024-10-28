# # ENCAPSULATION: Wrapping/binding of data members and methods
# # as well as hide the data using access specifiers in single unit.
# class A1:
#     a=100
#     _b=200
#     __c=None
#     print(a, " ",_b," ",__c)
#     def __add(self):
#         self.__c=self.a+self._b
#         print("Addition=",+self.__c)
#
#         # print(self.__c)  here u can call this private variable inside the same class
#
#
# obje=A1()
# obje._A1__add()
# print(obje._A1__c)   # when u want to call outside the class private variable then use (obj._classname__variblename)
#                         # is called mengling.


#########################################################################################################

# use getters and setters methods for encapsulation
# getters method:is used to Access the private data
# setters methods: To set or to modify the values.

class student:
    def __init__(self,name,roll_no,age):
        self.name=name
        self._roll_no=roll_no
        self.__age=age

    def get_age(self):
        return self.__age

    def set_age(self,age):
        if age>35:
            print("age is greater than 35")
        else:
            return self.__age

obj=student("amit",2,85)
print(obj.get_age())
(obj.set_age(20))
print(obj.get_age())

















