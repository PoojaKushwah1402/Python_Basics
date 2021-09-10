# Using Asterisk*
# If the number of variables is less than the number of values, 
# you can add an * to the variable name and the values will be assigned to the variable as a list:

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)#apple
print(yellow)#banana
print(red)#['cherry', 'strawberry', 'raspberry']

#If the asterisk is added to another variable name than the last, Python will assign values to 
#the variable until the number of values left matches the number of variables left.

