# String Stripping and Justifying

# Task: Given the string s, use string methods to:
# Remove leading/trailing spaces: remove all leading and trailing whitespace characters from the string.
# Left justify with '*': left justify the string within a field of width 20, using * as the fill character.
# Right justify with '*': right justify the string within a field of width 20, using * as the fill character.
s:str ="   Python is fun!   "
stripped_string = s.strip()

print('Remove Spaces:',stripped_string)
left_justify = stripped_string.ljust(20,'*') #The total length is 20 characters. Asterisks (*) will be included only when the character count is less than 20
right_justify = stripped_string.rjust(20,'*')

print('Left Justify:', end='\t')
print(left_justify)
print('Right Justify:', end='\t')
print(right_justify)



