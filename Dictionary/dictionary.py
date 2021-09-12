# # Dictionaries are used to store data values in key:value pairs.
# # A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

thisdict = {
    "year": 1964,
    "brand": "Ford",
    "model": "Mustang",
}
print(thisdict)

# Dictionary items are ordered, changeable, and does not allow duplicates.
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
print(len(thisdict))
x = thisdict.get("model")

#The keys() method will return a list of all the keys in the dictionary.
x = thisdict.keys()

# The values() method will return a list of all the values in the dictionary.
x = thisdict.values()

# The items() method will return each item in a dictionary, as tuples in a list.
x = thisdict.items() #dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

# The update() method will update the dictionary with the items from the given argument.
# The argument must be a dictionary, or an iterable object with key:value pairs.
# Update the "year" of the car by using the update() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})