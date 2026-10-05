#Name: Matthew Ward
#Class: 6th Hour
#Assignment: HW9
from HW8 import Student_list

#1. Print Hello World!
print("Hello World")

#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.
matts_car_dictionary = {
    "brand" : "ford",
    "model" : "F-150",
    "year" : [2004,2006,2010]}

#3. Print the keys of the dictionary from #2.
print(matts_car_dictionary)

#4. Print the values of the dictionary from #2
print(matts_car_dictionary.values())

#5. Print one of the three numbers from the list by itself
print(matts_car_dictionary["year"][2])

#6. Using the update function, add a fourth key to the dictionary and give it a value
matts_car_dictionary.update({"model" : "F-150,F-250"})

#7. Print the entire dictionary from #2 with the updated key and value.
print(matts_car_dictionary)

#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.
sixth_hour_class = {
    "student_1" : {
        "Name" : "Tucker",
        "Grade" : 12,
        "Sport" : False,
    },
    "student_2" : {
        "Name" : "Matt",
        "Grade" : 12,
        "Sport" : False,
    },
    "student_3" : {
        "Name" : "Owen",
        "Grade" : 12,
        "Sport" : False,
    },
}

#9. Print the names of all three classmates on the same line.
Student_name_list = [
    "Tucker",
    "Matt",
    "Owen",
]
print(Student_name_list)

#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.
sixth_hour_class.pop("student_1")
print(sixth_hour_class)