total_rows=int(input("enter no of rows: "))

for rows in range(1,total_rows+1):
    for column in range(1,total_rows+1):
        if (column==1)or(rows==total_rows)or(column==rows):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

'''
OUTPUT
enter no of rows: 5
*         
* *       
*   *     
*     *   
* * * * * 
'''