no_of_rows=int(input("Enter num of rows :"))

for row_no in range(1,no_of_rows+1):
    for column in range(1,row_no+1):
        print("* ",end="")
    print()

'''
or use below 

for row_no in range(1,no_of_rows+1):
    print("* "*row_no)
    
'''

'''
OUTPUT:
    
Enter num of rows :5
* 
* * 
* * * 
* * * * 
* * * * * 
'''