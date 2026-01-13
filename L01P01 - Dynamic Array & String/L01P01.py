# Dynamic Array Declaration
# varialbe = [value1, value2, ...]
l = []

# Add an element
l.append(5)
"""
0   1   2   3   4   5   ...
5   .   .   .   .   .   ...
"""

# Insert an element
# insert(pos, obj)
l = [5, 7, 8, 3, 6]
l.insert(2, 9)
print(l) 
#  0  1  2  3  4  5
# [5, 7, 9, 8, 3, 6]

# Get length
# len(obj)
l = [5, 7, 8, 3, 6]
n = len(l)
print(n) # 5

# Access elements in a dynamic array
# l[index]
l = [5, 7, 8, 3, 6]
result = l[2]
print(result) # 8
l[-1] = 9
# [5, 7, 8, 3, 9]

# Delete last element
# pop()
l.pop()
print(l) # [5, 7, 8, 3]

# Delete an element based on position
# pop(pos)
l.pop(2) # [5, 7, 3, 6]

# Remove all elements
# clear()
l.clear()


# Increase size
# extend(list)
l = [5, 7, 8, 3, 6]
l.extend(2*[0])
print(l) # [5, 7, 8, 3, 6, 0, 0]


# Decrease size
# slicing
l = l[0:2]
print(l) # [5, 7]


# Check if dynamic array is empty
l = []
if len(l) == 0:
    print("DA is empty!")
else:
    print("DA is not empty!")
    
# Loop through DA
l = [5, 7, 8, 3, 6]
for i in range(len(l)):
    print(l[i], end=", ")
# 5, 7, 8, 3, 6,
print("\n")
# Reverse loop in DA
l = [5, 7, 8, 3, 6]
for i in range(len(l) - 1, -1, -1):
    print(l[i], end=", ")
# 6, 3, 8, 7, 5,

#####################################
# String
s = ""

# Basic functions
"""
    1. len(s): Get the size of string
    2. if len(s) == 0: Use comparison to check if string is empty
    3. s = "": Use assignment to remove all values inside a string
    4. inserting: string0 = string0[:pos] + string1 + string0[pos:]
    5. deleting: string = string[:start_pos] + string[end_pos:]
    6. find(string): search string
    7. get substring: variable[start_pos:end_pos]
    8. merging: use "+" to concat strings
"""

# Checking characters
s = "123abc"
if ord(s[0]) >= 48 and ord(s[0]) <= 57:
    print("digit")
# log: digit


# Checking if characters are alphabet
s = "Programming"
result = s[1].isalpha()
print(result)
# log: True

# Other functions:
# isdigit
# islower
# isupper

# Convert string to numbers
# int(string)
# float(string)
s = "12"
number = int(s)
print(number)
# log: 12

# Convert number to string
number = 15789
s = str(number)
print(s)
# log: 15789

# uppercase and lowercase - built-in function
s = "algorithm"
c = s[2].upper()
print(c)
# log: G

# uppercase and lowercase - ascii approach (not recommended)
s = "algorithm"
c = chr(ord(s[2]) - 32)
print(c)
# log: G