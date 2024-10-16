# multilevel inheritence means aquaring properties from grandparent to parent to child

class grandmother:
    def cook(self):
        print("i can cook well")
    def sing(self):
        print("i can sing hindi song")
    def dance(self):
        print("grandmother can teach dance")
class mother(grandmother):
    def dance(self):
        print("i can dance")

class son(mother):
    def swim(self):
        print("i can swim")
    def dance(self):
        grandmother.dance(self)  # we can use this syntax also for calling same methods in child class
        mother.dance(self)   
        # super().dance()   # if you want dance method from mother also then u use super keyword
        print("i cannot dance")

son_1=son()     #here we can use all properties by mother as well as grandmother class.
# son_1.swim()
son_1.dance()
# son_1.sing()