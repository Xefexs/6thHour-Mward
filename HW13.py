#Name: Matthew Ward
#Class: 6th Hour
#Assignment: HW13

#1. Import the random function
import random
#2. Create a variable called 'temp' that randomly generates a number between 1 and 30
temp= random.randint(1,30)
print(temp)
#3. Go to the link below and convert the flowchart into pseudocode in comments, then code the flowchart completely:
#https://adacomputerscience.org/images/content/computer_science/design_and_development/program_design/figures/ada_cs_design_flow_ifelseif.svg
#Make if statement that checks if temp is more than 20
#   - If more, print it's hot
#   - If less, go to next if statement

#Make if statement that checks if temp is more than 10
#   - If more, print it's mild
#   - If less, print it's cold

#Print thank you, and end the code

if temp > 20:
    print("It's hot")
elif temp > 10 :
    print("It's mild")
else :
    print("It's cool")
print("Thank You")