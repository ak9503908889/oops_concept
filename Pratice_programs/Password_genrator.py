# create a strong password by using symbo,numbers,letters.

import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
         'p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H',
           'I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','2','3','4','5','6','7','8','9','1']
symbols=['!','@','#','$','%','*','&']
print("WELCOME TO PASSWORD GENRATOR")
n_letters=int(input("how many letters you want in your password?\n")) #4
n_numbers=int(input("how manu numbers you want in your password?\n"))
n_symbols=int(input("how many symbols you want in your password?\n"))
password_list=[]
for i in range(1,n_letters+1): # range function -1 count karte so +1 add kele because suppose 4 leeter pahije astil tr range 5 pahije.
    char=random.choice(letters) #pahile 4 charater randon yenar leeters madhun aani list madhe add honar.
    password_list += char
print(password_list)

for i in range(1,n_numbers+1):
    char=random.choice(numbers)
    password_list += char
print(password_list)

for i in range(1,n_symbols+1):
    char=random.choice(symbols)
    password_list += char
print(password_list)

random.shuffle(password_list)  # shuffle means jo password create zaly to again change hoto only char position change hote.
print(password_list)

final_password=""          # ethe only password list madhun string madhe convert sathi he kele.
for char in password_list:
    final_password+=char
print(final_password)
