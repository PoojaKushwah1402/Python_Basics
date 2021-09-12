# JSON in Python
# Python has a built-in package called json, which can be used to work with JSON data.
#Convert from JSON to Python:
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y)
print(type(x))#<class 'str'>

# Convert from Python to JSON
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(type(y),type(x))

print(type(json.dumps({"name": "John", "age": 30})))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(type(json.dumps(True)))
print(type(json.dumps(False)))
print(type(json.dumps(None)))


# Python	JSON
# dict	Object
# list	Array
# tuple	Array
# str	String
# int	Number
# float	Number
# True	true
# False	false
# None	null

# Format the Result
# The example above prints a JSON string, but it is not very easy to read, with no indentations 
# and line breaks.
# The json.dumps() method has parameters to make it easier to read the result:
#Use the indent parameter to define the numbers of indents:
# json.dumps(x, indent=4)
# you can also define the separators, default value is (", ", ": "), which means using a comma and a 
# space to separate each object, and a colon and a space to separate keys from values:
# Use the separators parameter to change the default separator:

json.dumps(x, indent=4, separators=(". ", " = "))

# Order the Result
# The json.dumps() method has parameters to order the keys in the result:
# Use the sort_keys parameter to specify if the result should be sorted or not:

json.dumps(x, indent=4, sort_keys=True)