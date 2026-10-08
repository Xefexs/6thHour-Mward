#Name: Matthew Ward
#Class: 6th Hour
#Assignment: HW11
import random

#1. Print "Hello World!"
print("Hello World")

#2. Create a list with three values that each randomly generate a number between 1 and 100
a = random.randint(1,10),random.randint(1,10),random.randint(1,10)

#3. Print the list.
print(a)

#4. Create an if statement that determines which of the three numbers is the highest and prints the result.
if a[0] >= a[1] and a[0] >= a[2]:
    print("list A 1 is greater than list A 2 and 3")
    num = a[0]
elif a[1] >= a[0] and a[1] >= a[2]:
    print("list A 2 is greater than list A 1 and 3")
    num = a[1]
elif a[2] >= a[0] and a[2] >= a[1]:
    print("list A 3 is greater than list A 1 and 2")
    num = a[2]

#5. Tie the result (the largest number) from #4 to a variable called "num".
print(num)

#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.
if num % 2 and num % 3:
    print("Num is divisible by both 2 and 3")
elif num % 2:
    print("Num is divisible by 2")
elif num % 3:
    print("Num is divisible by 3")
else :
    print("Num isn't divisible by 2 or 3")