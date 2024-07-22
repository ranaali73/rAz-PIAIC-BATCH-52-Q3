# Age Assignments Based on the Riddle

# Problem Statement: Write a program to solve this age-related riddle! Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:
# Anton is 21 years old.
# Beth is 6 years older than Anton.
# Chen is 20 years older than Beth.
# Drew is as old as Chen's age plus Anton's age.
# Ethan is the same age as Chen.
# Your code should store each person's age to a variable and print their names and ages at the end.
# Anton is 3
# Beth is 4
# Chen is 5
# Drew is 6
# Ethan is 7

antons_age = 21
beths_age = antons_age + 6 
chens_age =  beths_age + 20
drews_age = chens_age + antons_age
ethans_age = chens_age

friends_age = f'Anton is {antons_age} \n Beth is {beths_age} \n Chen is {chens_age} \n \
Drew is {drews_age} \n Ethan is {ethans_age}' 
print(friends_age)