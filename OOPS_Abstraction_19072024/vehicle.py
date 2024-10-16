
from abstract_class import vehicle

class bike(vehicle):
    def __init__(self,n,color):
        super().__init__(n)  # we are create this constructer super beacsue when we call vehicle class
        self.color=color                           # there is also one own constructor.
    def start(self):
        print("start with kick")

# class Scooty(vehicle):
#     def __init__(self,n):
#         self.no_of_tyers =2
#     def start(self):
#         print("start with self")

class car(vehicle):
    def __init__(self,n,k):
        super().__init__(n)
        self.numof_gears=5

    def start(self):
        print("start with key")



