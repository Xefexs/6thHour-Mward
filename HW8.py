#Name: Matthew Ward
#Class: 6th Hour
#Assignment: HW8
#TEST COMMENT TO SEE IF GIT WORKS 2 ELECTRIC BOOGALOO

#1. Import the "random" library
import random

#2. print "Hello World!"
print("Hello World!")

#3. Create three different variables that each randomly generate an integer between 1 and 10
roll1 = random.randint(1,10)
roll2 =  random.randint(1,10)
roll3 = random.randint(1,10)

#4. Print the three variables from #3 on the same line.
print (roll1, roll2, roll3)

#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
roll1 += 2
roll2 -= 4
roll3 *= 1.5

#6. Print each result from #5 on the same line.
print (roll1, roll2, roll3)

#7. Create a list containing four variables that each randomly generate an integer between 1 and 6
rand_list = [random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]

#8. Sort the list in #7 and print it.
rand_list.sort(reverse=True)
print (rand_list)

#9. Add together the highest three numbers in the list from #7 and print the result.
X = (rand_list[0]+rand_list[1]+rand_list[2])
print (X)

#10. Create a list with 5 names of other students in this class and print the list.
Student_list = ["Cody","Matthew","Tucker","Owen","Owyn"]
print (Student_list)

#11. Shuffle the list in #10 and print the list again.
random.shuffle (Student_list)
print (Student_list)

#12. Print a random choice from the list of names from #10.
class_num_choice = random.choice(Student_list)
print(class_num_choice)