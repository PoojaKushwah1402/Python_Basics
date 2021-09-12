# #In Python a function is defined using the def keyword:

# x = "awesome"
# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)
# myfunc()
# print("Python is " + x)

# #To create a global variable inside a function, you can use the global keyword.
# #Also, use the global keyword if you want to change a global variable inside a function.


# def myfunc1():
#   global k
#   k = "fantastic"
#   global x
#   x = "fantastic11"
# myfunc1()
# print("Python is " + k)

# Number of Arguments
# By default, a function must be called with the correct number of arguments. Meaning that if your 
# function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.

# From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.

# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the 
# parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:

# def my_function(*kids):
#   print("The youngest child is " , kids)
# my_function("Emil", "Tobias", "Linus")

# # Keyword Arguments
# # You can also send arguments with the key = value syntax.
# # This way the order of the arguments does not matter.

# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)
# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk:
# ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:
def my_function(**kid):
  print("His last name is " ,kid)
my_function(fname = "Tobias", lname = "Refsnes")