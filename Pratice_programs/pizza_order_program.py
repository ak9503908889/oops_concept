# if you want to order pizza with small,medium,large sizes and want to calcualte bill as per size
# and u also want to add peporoni and extra cheese on it and add that price in that
# as per above scenario create a program and claculate on random bill.


size=input("what size of pizza you want(S,M,L)=? ")
bill=0

if size=='S'or size=='s':
    bill+=100
    print("Small pizza price is 100 RS ")
elif size=='M'or size=='m':
    bill+=200
    print("Medium pizza price is 200 RS ")
else:
    bill +=300
    print("Large pizza price is 300 RS ")

Add_pepproni=input("Do u want pepproni(Y/N)=? ")
if Add_pepproni=='Y'or Add_pepproni=='y':
    if size=='S'or size=='s':
        bill+=20
    elif size=='m'or size=='M':
        bill+=30
    else:
        bill+=50
Add_extra_cheese=input("Do you want to add extra cheese(Y/N)=? ")
if Add_extra_cheese=='Y'or Add_extra_cheese=='y':
    bill+=20

print(f"Your final bill is {bill}")