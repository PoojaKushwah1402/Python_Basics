# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, 
# the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.

thistuple = ("apple", "banana", "cherry")
print(thistuple)
#Tuple items are ordered, unchangeable, and allow duplicate values.
#Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

# Create Tuple With One Item
# To create a tuple with only one item, you have to add a comma after the item,
#  otherwise Python will not recognize it as a tuple. 
#Tuple items can be of any data type:
#A tuple can contain different data types:
#It is also possible to use the tuple() constructor to make a tuple.

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#You can access tuple items by referring to the index number, inside square brackets:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
#Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
#Tuples are unchangeable, or immutable as it also is called.
# Since tuples are immutable, they do not have a build-in append() method, but there are other ways to 
#add items to a tuple.
# 1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, 
#add your item(s), and convert it back into a tuple.
# 2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, 
#(or many), create a new tuple with the item(s), and add it to the existing tuple:

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
#Or you can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists