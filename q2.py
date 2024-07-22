# Formatted String Interpolation

# Task: Given the variables name, age, and city, use f-strings to construct a sentence that describes a person using these variables.
name:str = "Alice"
age:int = 30
city:str = "New York"

bio = f'{name} is {age} years old and lives in {city}.'
print(bio)