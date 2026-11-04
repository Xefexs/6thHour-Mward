#Name: Matthew Ward
#Class: 6th Hour
#Assignment: HW14
import random
import time

#1. Create a while loop with variable i that counts down from 5 to 0 and then prints
#"Hello World!" at the end.
j = 5
while j >= 0:
    print(j)
    j -= 1
print("Hello World")


#2. Create a while loop that prints only even numbers between 1 and 30 (HINT: modulo).
k = 1
while k <= 30:
    if k % 2 == 0:
        print(k)
    k+=1


#3. Create a while loop that prints from 1 to 30 and continues (skips the number) if the
#number is divisible by 3.
s = 1
while s <= 30:
    if s % 3 == 0:
        s += 1
        continue
    print(s)
    s += 1

#4. Create a while loop that randomly generates a number between 1 and 6, prints the result,
#and then breaks the loop if it's a 1.
l=0
while l!=1:
    l=random.randint(1,6)
    print(l)
l=random.randint(1,6)


#5. Create a while loop that asks for a number input until the user inputs the number 0.
n= int(input("enter a number"))
while n>=1:
    n = (int(input("enter a number")))