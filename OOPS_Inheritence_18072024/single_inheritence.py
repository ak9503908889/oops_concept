#1. what is inheritence -Aquaring properties of base class into derived class..1
# reusability of code we can say
# Single inheritence- Inherite properties from one  parent/base/super class to single child class.


class human:
    def eat(self):
        print("i can eat")
    def work(self):
        print("i can work")
class male:
    def eat(self):
        print("i can eat")
    def work(self):
        print("i can work")
male_1= male()
male_1.eat()

# 2----------in below code we dont write repeted code in male class instead of that we
# aquring properties of human class by inheritence.
class human:
    def eat(self):
        print("i can eat")
    def work(self):
        print("i can work")
class male(human):
  pass
male_1= male()
male_1.eat()

#-3---------------------------------------------
class human:
    def eat(self):
        print("i can eat")
    def work(self):
        print("i can work")
class male(human):
  def flirt(self):
      print("i can flirt")  # own method we can use
male_1= male()
male_1.eat()          #class human method we called here
male_1.flirt()      # class male own method we are called here

#4--method overrideen cocept so use super() keyword,
class human:
    def eat(self):
        print("i can eat")
    def work(self):
        print("i can work")
class male(human):
    def eat(self):
        print("i can eat")
    def work(self):
        print("i can code")     # method name  same but work approach diffrent

male_1= male()
male_1.eat()
male_1.work()  # here after run it will give i can code by male class approach only
                 # if you want human class work method implementaion then need to use super()method.

#4--------------------------------
class human:
    def eat(self):
        print("i can eat")
    def work(self):
        print("i can work")
class male(human):
    def eat(self):
        print("i can eat")
    def work(self):
        super().work()  # use super() for both approach if u want together.
        print("i can code")

male_1= male()
male_1.eat()
male_1.work()