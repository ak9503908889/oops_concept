# getters: we are using getters for get the private data
# setters: we are using setters for modify

class Amit:
    def __init__(self,name,roll_no,age):
        self.name=name
        self._roll_no=roll_no
        self.__age=age

    def get_age(self):
        return self.__age

    def set_age(self,age):
        # self.__age=age
        if (age > 35):
            print("age is greater than 35")
        else:
            self.__age=age


obj=Amit("pratik",12,30)
print(obj.get_age())   # it gives first 30
obj.set_age(39)         # again set 35
print(obj.get_age())      # again change 35

