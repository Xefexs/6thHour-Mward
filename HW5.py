#Name:Matthew Ward
#Class: 6th Hour
#Assignment: HW5

#1. Print Hello World!
print("hello world")
#1. Create a list with 5 strings containing 5 different names in it.
name_list = ["jake","jackson","abby","tucker","matthew"]

print(name_list)

#2. Append a new name onto the Name List.
name_list.append("owen")
print(name_list)

#3. Print out the 4th name on the list.
print (name_list[3])

#4. Create a list with 4 different integers in it.
num_list = [1,2,3,4,5]
print(num_list)

#5. Insert a new integer into the 2nd spot and print the new list.
num_list.insert(1,6)
print(num_list)

#6. Sort the list from lowest to highest and print the sorted list.
num_list.sort()
print(num_list)

#7. Add the 1st three numbers on the sorted list together and print the sum.
num_list_subsum = num_list[0] + num_list[1] + num_list[2]
print(num_list_subsum)

#8. Create a list with two strings, two integers, and two boolean values.
list_int = ["hello","world",9,18,True,False ]
print(list_int)

#9. Create a print statement that asks the user to input their own index value for the list on #8.

print(list_int[int(input("Choose an index value: "))])