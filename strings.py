#strings in Python are arrays of bytes representing unicode characters.

var1 = 'Hello there!'
str1 = 'P o o j a'
var2 = 'Hello "there"!'
var3 = "pooja's there!"
var4 = '''
this is multi line text
you got it;
:') 
there you go
'''
# print(var1,var2,var3,var4)
print(str1[1],' -', str1[-3]) #negative index will give you last values
print(var2[2:6]) #will return all the value from index 2 to 5 
k = "banana"
for x in k:
  print(x)
print(len(k))
txt = "The best things in life are free!"
print("free" in txt)

"""Since Python will ignore string literals that are not assigned to a variable, 
you can add a multiline string (triple quotes) in your code, and place your comment inside it:"""

'''String Length : 
To get the length of a string, use the len() function.'''
#The strip() method removes any whitespace from the beginning or the end:
#The replace() method replaces a string with another string:

# The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#The format() method takes the passed arguments, formats them, and 
#places them in the string where the placeholders {} are:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
txt = "We are the so-called \"Vikings\" from the north."
print(txt)