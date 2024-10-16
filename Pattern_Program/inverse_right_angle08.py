total_rows=int(input("enter total number of rows: "))

for row_no in range(1,total_rows+1):
    # here first display spaces
    for spaces in range(1,(total_rows-row_no)+1):
        print(" ",end=" ")
    # here now print star
    for symbol in range(1,row_no+1):
        print("*",end=" ")
    print()

'''
condition1: find spaces= total no pf rows-rowsno
condition2: find star present in that rows= row no fetch
enter total number of rows: 5
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
'''

