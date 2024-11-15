# if string1="cat"  and string2="act" so this strings are anagram why beacause
# length of strings are same as well as charter should be same in both string

string1="amit"
string2="mita"

if len(string1)==len(string2):
    if sorted(string1)==sorted(string2):
        print("the both strings are anagram")
    else:
        print("not anagram")
else:
    print("not anagram")

