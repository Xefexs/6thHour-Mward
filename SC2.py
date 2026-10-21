#Name: Matthew Ward
#Class: 6th Hour
#Assignment: SC2


#A local health clinic is looking to add a quick BMI calculator to their website so that their
#patients can quickly input their height and weight and be told their BMI as well as their
#classification. The classifications are as follows:

# - Underweight: Less than 18.5 BMI
# - Normal Weight: 18.5 to 24.9 BMI
# - Overweight: 25 to 29.9 BMI
# - Obese: 30 or more BMI

#It is up to you to figure out the calculation for an accurate BMI reading and tying it to
#the right classification
weight =int(input("Enter weight in lb"))
height = int(input("Enter height in inches"))
height2 = height*height
bmi = weight/height2
bmi2 = bmi*703
if bmi2 < 18.5:
    print("You are underweight",bmi2)
elif bmi2 >= 18.5 and bmi2 <= 24.9:
    print("You are normal weight",bmi2)
elif  bmi2 >= 25 and bmi2 <= 29.9:
    print("You are overweight",bmi2)
else:
     print("You are obese",bmi2)