# if All friends have arrange one party and everyone wants to pay bill then you choose random person
#for that scenario create a program.

import random
names=input("enter everybody name seperated by comma: ")
names_list=names.split(",")
#print(names_list)
length=len(names_list)
random_choice=random.randint(0,length-1)
print(f"{names_list[random_choice]}  will pay the bill ")

