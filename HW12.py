#Name: Matthew Ward
#Class: 6th Hour
#Assignment: HW12

import random

#1. Print Hello World!
print("Hello World")

#2. Create three different boolean variables named wifi, login, and admin.

wifi = random.choice([True, False])
Admin = random.choice([True, False])
login = random.choice([True, False])

#3. Create a separate integer variable that denotes the number of times
#someone with admin credentials has logged in.
Admin_login = 145
print(Admin_login)
#4. Create a nested if statement that checks to see if wifi is true,
#login is true, and admin is true. If they are all true, print a
#welcome message and increase the integer variable by one. If one of them
#is false, print an error message telling them which one they are "missing".
if wifi == True :
    if login == True :
        if Admin == True :
            print("Admin is connected")
            Admin_login += 1
            print(Admin_login)
        else :
            print("Error NO ADMIN CONNECTED")
    else:
        print("ERROR COULD NOT CONNECT")
else:
    print("ERROR NO WIFI CONNECTED")