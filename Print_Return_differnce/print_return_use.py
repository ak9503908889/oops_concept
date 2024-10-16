# print: is a function
# it stop the flow of execution
# it show the value to the user it is return none if u r not return the explicitly
#why used: if we simply print and not return that value so we cant use this value anywhere.

# return: is a keyword
# its change the flow of execution
# it does not show the value
# return is used only within fuction
#why used:u can use that return value in an another function as an argument

def fun1(a,b):
    c=a+b
    print(c)
output1=fun1(3,5)
print(output1)             # output is 8  none

def fun2(a,b):
    c=a+b
    return c
output2=fun2(3,5)
print(output2)               # output is only 8  because we return 8 value

def fun3(x):
    return x+5

output3=fun3(output2)        # here we can use fun2 value in fun3 because of use return .
print(output3)                # 8+5 =13 yeil