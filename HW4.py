#Name: Matthew ward
#Class: 6th Hour
#Assignment: HW4
import math

#1. Print "Hello World!"
print("Hello World")
#2. import the 'math' library
import math
#3. Create two variables, x and y, that asks the user for a decimal (float) for x and an integer for y.
x = int(input("Give me a number: "))
y = int(input("Give me another number: "))
#4. Create a variable with the value that is x and y added together.
int_sum = x + y
#5. Print the variable from #4.
print(int_sum)
#6. Create a variable with the value that is x and y added together, then divide the sum by 3.
int_div = int_sum / 3
#7. Print the variable from #6.
print(int_div)
#8. Create a variable with the value of the square root of y, then print the result.
int_sr = math.sqrt(x)
print(int_sr)
#9. Use the round function to round x to the nearest tenths place (EX: 1.17 rounds to 1.1). Print the result.
print(round(x,1))
#10. Use the ceiling function to round x up to the nearest whole number. Print the result.
print(math.ceil(3.14))
#11. Use the floor function to round x down to the nearest whole number. Print the result.
print(math.floor(3.99998))