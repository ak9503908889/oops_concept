# class ComplexNumber:
#     def __init__(self,r,i):
#         self.real=r
#         self.imaginary=i
#
# c1=ComplexNumber(1,2)
# c2=ComplexNumber(4,5)
# print(c1+c2)

# after run TypeError: unsupported operand type(s) for +: 'ComplexNumber' and 'ComplexNumber'
# so to resolve this we use __add__ method which is dunder method of (+ add )
#------------------------------------------------------------------------
class ComplexNumber:
    def __init__(self,r,i):
        self.real=r
        self.imaginary=i
    def __add__(self,other):
        return F"{self.real+other.real}+{self.imaginary+other.imaginary}i"

c1=ComplexNumber(1,2)
c2=ComplexNumber(4,5)
print(c1+c2)                     # output 5+7i

#--------------------------------------------------------------------------------------
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __gt__(self, other):      #this is called operator overloading greater than is use for dunder vali.
        if self.age>other.age:     # here int vali grater than operator use hote
            return True
        else:
            return False

p1=person("amit",25)
p2=person("pradip",20)

if p1>p2:
    print(f"{p1.name} will pay the bill")
else:
    print(f"{p2.name} will pay the bill")