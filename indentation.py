# Indentation refers to the spaces at the beginning of a code line.

# Where in other programming languages the indentation in code is for readability only, 
# the indentation in Python is very important.
if(5>2) : 
    print('success')

# if(5>2) : 
# prrint('success no')   wrong syntax

# You have to use the same number of spaces in the same block of code, 
# otherwise Python will give you an error:

if 5 > 2:
 print("Five is greater than two!") 
 print("Five is greater than two!") #correct same space

if 5 > 2:
        print("Five is greater than two! done") 
    print("Five is greater than two! done") #error no same space