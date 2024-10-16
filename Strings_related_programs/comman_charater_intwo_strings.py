str1="thins ticks"
str2="thick bricks"

comman_char=[]          # create empty list for use to collect comman char

for char in str1:
    if char in str2 and char!=' ' and char not in comman_char:
        comman_char.append(char)

comman_char.sort()

print(comman_char)         # list madhe milate output ['c', 'h', 'i', 'k', 's', 't']
print(''.join(comman_char))   #  chikst  he string madhe pahije asel tr.






# second  way to sort and find comman charater in two strings.
# def common_characters(str1, str2):
#     # Initialize an empty list to store common characters
#     common_chars = []
#
#     # Loop through each character in the first string
#     for char in str1:
#         # Check if the character is in the second string and not already added
#         if char in str2 and char not in common_chars:
#             common_chars.append(char)
#
#     # Sort the list of common characters alphabetically
#     common_chars.sort()
#
#     # Join the sorted list into a string
#     result = ''.join(common_chars)
#
#     return result
#
# # Example usage:
# str1 = "alphabet"
# str2 = "elephant"
# print("Common characters in alphabetical order:", common_characters(str1, str2))
