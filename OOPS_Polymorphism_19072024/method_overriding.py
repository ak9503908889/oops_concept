# METHOD OVERRRIDING : it is achieved by Inheritence. it also called runtime polymorphism
# In method overriding we define methods with same name same parameter in diffrent class .

class Father:
    def sleep(self):
        print("sleep from 10:00 PM to 5.00 AM")
    def eat(self):
        print("eating")
class Son(Father) :
    def sleep(self):
        print("sleep from 12.00 PM to 8.00 AM")  # here method override
        # super().sleep()  # we use if we want father sleep method also with son sleep method.




amit=Son()
amit.sleep()


