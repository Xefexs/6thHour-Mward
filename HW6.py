#Name: Matthew Ward
#Class: 6th Hour
#Assignment: HW6


#1. Create a list with 9 different numbers inside.
num_list = [15,12,5,6,32,4546,3432,6577,2355,]


#2. Sort the list from highest to lowest.
num_list.sort(reverse=True)


#3. Create an empty list.
empty_list = []

#4. Remove the median number from the first list and add it to the second list.
Var = num_list.pop(4)
empty_list.append(Var)

#5. Remove the first number from the first list and add it to the second list.
Var2 = num_list.pop(0)
empty_list.append(Var2)

#6. Print both lists.
print(num_list)
print(empty_list)

#7. Add the two numbers in the second list together and print the result.
add = Var + Var2
print(add)

#8. Add the sum from #7 to the first list.
num_list.append(add)

#9. Sort the first list from lowest to highest and print it.
num_list.sort()
print(num_list)