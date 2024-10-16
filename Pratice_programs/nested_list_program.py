# # nested list means the list within list
# list=[1,2,4,6,8,[5,2,8],7,2]
# # print(list)
#
# print(list[2])  # 4   use indexing  here
#
# print(list[5])   # [5, 2, 8]
#
# print(list[5][0]) # 5
# print(list[5][-1]) #8

# list=[1,2,4,6,8,['amit','divya','anushaka'],7,2]
#
# print(list[5][1])


# create list flatten
def flatten(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item,list):
            flat_list.extend(flatten(item)) # ethe recursion use hotey function la again call kartoy.flatten
        else:
            flat_list.append(item)
    return flat_list

# Example usage:
nested_list = [1, [2, [3,[4,5,8], 4], 5], [6, 7], [5,8,7],8]
flat_list = flatten(nested_list)
print(flat_list)