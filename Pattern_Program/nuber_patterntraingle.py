def print_diamond(n):
    # Upper half of the diamond
    for i in range(n):
        print(' ' * (n - i - 1), end='')
        for j in range(i + 1):
            print(j + 1, end='')
        for k in range(i):
            print(i - k, end='')
        print()
    # Lower half of the diamond
    for i in range(n - 2, -1, -1):
        print(' ' * (n - i - 1), end='')
        for j in range(i + 1):
            print(j + 1, end='')
        for k in range(i):
            print(i - k, end='')
        print()

n = int(input("Enter the number of rows: "))
print_diamond(n)
''' 
  1
 121
12321
 121
  1
'''