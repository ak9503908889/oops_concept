
Given_string=str(input("any string enter: "))
Given_string=Given_string.lower()

char_count={}
for char in Given_string:
    if char in char_count:
        char_count[char]+=1
    else:
        char_count[char]=1

print(char_count)

output = ''.join(f"{char}{count}" for char, count in char_count.items())
print(output)
'''any string enter: amit
{'a': 1, 'm': 1, 'i': 1, 't': 1}
a1m1i1t1'''

# for char,count in char_count.items():
#     print(f"{char}--{count}")

# /////////////////////////////////////////////////////////////////////////////////////
# def count_character_occurrences(input_string):
#     # Convert to lowercase
#     input_string = input_string.lower()
#
#     # Create a dictionary to store character counts
#     char_count = {}
#
#     # Iterate over each character
#     for char in input_string:
#         if char.isalpha():  # Only consider alphabets
#             if char in char_count:
#                 char_count[char] += 1
#             else:
#                 char_count[char] = 1
#
#     # Print character counts
#     for char, count in char_count.items():
#         print(f"{char}-{count}")
#
#
# input_string = "This is a sample test output"
# print("Input String:", input_string)
# print("Character Occurrences:")
# count_character_occurrences(input_string)





























