# what is multiple- one child get properties from two or more parent class.
class mother:
    def cook(self):
        print("i can cook well")

class father:
    def work(self):
        print("i can work ")

class boy(mother,father):  # here inherit both parent class properties into child
    pass

boy_1=boy()
boy_1.cook()
boy_1.work()

#2---if both parent having same method with diffrent approach then it will call that method first by considering
#order of class which we inherited
class mother:
    def cook(self):
        print("i can cook well")
    def sing(self):
        print("i can sing hindi song")

class father:
    def work(self):
        print("i can work ")

    def sing(self):
        print("i can sing marathi song")

class boy(mother,father):  # here inherit both parent class properties into child
    pass

boy_1=boy()
boy_1.sing()    #i can sing hindi song this is output here because mother class is first in order wise
                  # so it call sing method by mother class not father class.
father.sing(boy_1) # if u dont want to follow order then dirct u can call sing method of father .



#3------
class mother:
    def cook(self):
        print("i can cook well")
    def sing(self):
        print("i can sing hindi song")

class father:
    def work(self):
        print("i can work ")

    def sing(self):
        print("i can sing marathi song")

class boy(mother,father):  # here inherit both parent class properties into child
    pass
    def sing(self):
        print("i can sing english song")

boy_1=boy()
boy_1.sing()
print(boy.mro())   # this is method resolution order in python use for same methods name
                   # first boy method call then check order of class which is inherited.

