# hierarchical inheritence is one parent to multiple child we can inherite properties


class Human:
    def __init__(self,name,age):
        print(" calling init from Human class")
        self.name=name
        self.age=age
    def eat(self):
        print(" i can eat")


class Male(Human):
    def work(self):
        print(" i can work")

class Female(Human):
    def sleep(self):
        print("i cannot sleep more than 5 hr ")

female_1=Female("piya",25)  #if not gives attributes then it will give error.
female_1.eat()
print(female_1.name)
print(female_1.age)
# female_1.sleep()


# male_1=Male()
# male_1.work()
# male_1.eat()