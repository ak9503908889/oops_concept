from abc import ABC,abstractmethod  # its necessary for create abstarct class /method init

class vehicle(ABC):
    def __init__(self,n):
        self.no_of_tyers=n
    @abstractmethod            # use to create abstarct method
    def start(self):
        pass
    def dispaly(self):   # we can have normal/concrete method in abstarct class.
        print("hi i display")