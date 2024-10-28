# write a program to find max number in list by taking the numbers from user

numbers=input("Enter list of numbers: ")
#10 20 30 45 89
numbers_list=numbers.split()  # here we split the num by using space beacuse we want all num is in list .
print(numbers_list) # ['10', '20', '30', '45', '89'] we will get this output.
# but here will get the list of numbers in string format so for next step to convert them into int
# we use below range or for loop for access or traverse this list elements.
# for that we need range and for range we need count
count=0
for number in numbers_list:
    count +=1
print(f"the length of the list is : {count}")  # 0 1 2 3 4

for i in range(count):
    numbers_list[i]=int(numbers_list[i])
print(numbers_list)         #[10, 20, 30, 45, 89] now its in proper list format
# so we can find max number.
max_number=numbers_list[0]  # assume first number in o index is max
# print(max_number)
# now we itreate each no within list to above max number and find the original max number.
for num in numbers_list:
    if num > max_number:
        max_number=num
print(f"our final max number from list is:  {max_number}")
