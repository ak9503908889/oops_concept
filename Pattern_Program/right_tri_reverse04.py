no_of_rows=int(input("Enter num of rows :"))

for row_no in range(no_of_rows,0,-1):
    for column in range(1,row_no+1):
        print("* ",end="")
    print()


'''
Enter num of rows :4
* * * * 
* * * 
* * 
* 

'''