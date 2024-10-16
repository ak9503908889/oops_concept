# i want only duplicates num in given list and make new list
from itertools import count
list=[1,2,2,5,4,5,6,8,3,5,9]


empty_list=[]
for num in list:
    if list.count(num)>1 and num not in empty_list:
        empty_list.append(num)
print(empty_list)


# if i want to remove duplicate number in given list and make fresh list without duplicates

list=[1,2,2,3,6,8,4,9,4,6,5,68,9]

fresh_list_witout_duplicates=[]

for num in list:
    if num not in fresh_list_witout_duplicates:
        fresh_list_witout_duplicates.append(num)
print(fresh_list_witout_duplicates)