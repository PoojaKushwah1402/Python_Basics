# Iterating Arrays
# Iterating means going through elements one by one.
# As we deal with multi-dimensional arrays in numpy, we can do this using basic for loop of python.
# If we iterate on a 1-D array it will go through each element one by one.
import numpy as np

arr = np.array([1, 2, 3])
for x in arr:
  print(x)

# Iterating 2-D Arrays
# In a 2-D array it will go through all the rows.
# Iterate on the elements of the following 2-D array:

arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  print(x)

# To return the actual values, the scalars, we have to iterate the arrays in each dimension.
# Example
# Iterate on each scalar element of the 2-D array:

arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  for y in x:
    print(y)

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
  print(x)

# Iterating Arrays Using nditer()
# The function nditer() is a helping function that can be used from very basic to very advanced iterations. 
# It solves some basic issues which we face in iteration, lets go through it with examples.
# Iterating on Each Scalar Element In basic for loops, iterating through each scalar of an array 
# we need to use n for loops which can be difficult to write for arrays with very high dimensionality.

#Iterate through the following 3-D array:

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
  print(x)