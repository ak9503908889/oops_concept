""" if given is [4,5,7,11,9,13,8,12]  and i want the pair of elements in this
list which sum is 20 like [11,9], [12,8] in python """

# given list
arr = (4, 5, 7, 11, 9, 13, 8, 12)
target_sum = 20

# Initialize an empty set to store numbers we've seen
seen_numbers = set()

# Loop through each element in the list
for num in arr:
    # Calculate the number needed to reach the target sum
    required_sum = target_sum - num     # 16,15,13,9,11,7,12,8   no

    # Check if the complement exists in the set                 (11,9),(13,7)
    if required_sum in seen_numbers:
        print((required_sum, num))

    # Add the current number to the set
    seen_numbers.add(num)

"""
Dry Run:
Initial Setup:

arr = [4, 5, 7, 11, 9, 13, 8, 12]
target_sum = 20
seen = {} (empty set)
First Iteration (num = 4):

complement = 20 - 4 = 16
16 is not in seen (since seen is empty).
Add 4 to seen: seen = {4}.
Second Iteration (num = 5):

complement = 20 - 5 = 15
15 is not in seen.
Add 5 to seen: seen = {4, 5}.
Third Iteration (num = 7):

complement = 20 - 7 = 13
13 is not in seen.
Add 7 to seen: seen = {4, 5, 7}.
Fourth Iteration (num = 11):

complement = 20 - 11 = 9
9 is not in seen.
Add 11 to seen: seen = {4, 5, 7, 11}.
Fifth Iteration (num = 9):

complement = 20 - 9 = 11
11 is in seen! This means we've found a valid pair.
Output: [11, 9].
Add 9 to seen: seen = {4, 5, 7, 9, 11}.
Sixth Iteration (num = 13):

complement = 20 - 13 = 7
7 is in seen! This means we've found another valid pair.
Output: [7, 13].
Add 13 to seen: seen = {4, 5, 7, 9, 11, 13}.
Seventh Iteration (num = 8):

complement = 20 - 8 = 12
12 is not in seen.
Add 8 to seen: seen = {4, 5, 7, 8, 9, 11, 13}.
Eighth Iteration (num = 12):

complement = 20 - 12 = 8
8 is in seen! This means we've found another valid pair.
Output: [8, 12].
Add 12 to seen: seen = {4, 5, 7, 8, 9, 11, 12, 13}.
Final Output:
csharp
Copy code
[11, 9]
[7, 13]
[8, 12]
"""

"""we can use below code also but not using list because list is slower than set and set handle duplicate well
so we use set above
seen = []

 # Loop through each element in the list
for num in arr:
     complement = target_sum - num

     if complement in seen:
         print([complement, num])

     seen.append(num) """