# Python Dates
# A date in Python is not a data type of its own, but we can import a 
# module named datetime to work with dates as date objects.

import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))

# Creating Date Objects
# To create a date, we can use the datetime() class (constructor) of the datetime module.
# The datetime() class requires three parameters to create a date: year, month, day.
x = datetime.datetime(2020, 5, 17)

print(x)
print(x.strftime("%B"))

# The strftime() Method
# The datetime object has a method for formatting date objects into readable strings.
# The method is called strftime(), and takes one parameter, format, to specify the format of 
# the returned string: