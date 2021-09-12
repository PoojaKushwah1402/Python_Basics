# Python supports the usual logical conditions from mathematics:
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

# The pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content, 
#put in the pass statement to avoid getting an error.
a = 33
b = 200
if b > a:
  pass


# Elif
# The elif keyword is pythons way of saying "if the previous conditions were not true, then
#  try this condition".
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# Short Hand If
# If you have only one statement to execute, you can put it on the same line as the if statement.
if a > b: print("a is greater than b")

# Short Hand If ... Else
# If you have only one statement to execute, one for if, and one for else, you can put it all on the same 
#line:
a = 2
b = 330
print("A") if a > b else print("B")

# One line if else statement, with 3 conditions:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# Test if a is greater than b, AND if c is greater than a:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")