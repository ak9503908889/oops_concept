no_of_rows=int(input("Enter num of rows :"))
ch=64  # here ch=65 but it starts from B so take 64 we want start from A
for row_no in range(1,no_of_rows+1):
    for column in range(1,row_no+1):
        print("{0}".format(chr(ch+row_no)),end=" ")
    print()


'''
when use row_no will get below
 Enter num of rows :5
A 
B B 
C C C 
D D D D 
E E E E E '''

'''
when use column: print("{0}".format(chr(ch+column)),end=" ")

then output look like:

Enter num of rows :5
A 
A B 
A B C 
A B C D 
A B C D E  
'''

'''
no_of_rows=int(input("Enter num of rows :"))
ch=64  # here ch=65 but it starts from B so take 64 we want start from A
for row_no in range(1,no_of_rows+1):
    for column in range(1,row_no+1):
        ch=ch+1
        print("{0}".format(chr(ch)),end=" ")
    print()

OUTPUT    
Enter num of rows :3
A 
B C 
D E F 
'''