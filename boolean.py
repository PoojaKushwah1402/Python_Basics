# Booleans represent one of two values: True or False.
# In fact, there are not many values that evaluate to False, 
# except empty values, such as (), [], {}, "", the number 0, and the 
# value None. And of course the value False evaluates to False.

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# One more value, or object in this case, evaluates to False, and 
# that is if you have an object that is made from a class with a __len__ function that returns 0 or False:

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

# Python also has many built-in functions that return a boolean value, like the isinstance() 
# function, which can be used to determine if an object is of a certain data type:

x = 200
print(isinstance(x, int))