# String Splitting and Joining

# Task: Given the string s, use string methods to:
# Split into a list: break the string into a list of substrings based on the delimiter ,.
# Join with spaces: combine the list of substrings back into a single string, with each element separated by a space.
s:str ="apple,banana,cherry,dates"
split_string = s.split(',')
join_string = ' '.join(split_string)
print('Split:',split_string)
print('Join:',join_string)