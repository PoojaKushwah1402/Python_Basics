# Set is one of 4 built-in data types in Python used to store collections of data.
# A set is a collection which is both unordered and unindexed.
# Sets are written with curly brackets.
# Set items are unordered, unchangeable, and do not allow duplicate values.
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
# Sets cannot have two items with the same value.
#**Once a set is created, you cannot change its items, but you can add new items.

thisset = {"apple", "banana", "cherry"}
thisnewset = set(("apple", "banana", "cherry",'banana')) # note the double round-brackets
print(thisset,thisnewset)

# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, or ask if a specified value is 
# present in a set, by using the in keyword.
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)