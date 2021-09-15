# Shape of an Array
# The shape of an array is the number of elements in each dimension.
# Get the Shape of an Array
# NumPy arrays have an attribute called shape that returns a tuple with each index having the number of 
# corresponding elements.
import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('shape of array :', arr.shape)

# What does the shape tuple represent?
# Integers at every index tells about the number of elements the corresponding dimension has.
# In the example above at index-4 we have value 4, so we can say that 5th ( 4 + 1 th) dimension has 4 elements.


# Reshaping arrays
# Reshaping means changing the shape of an array.
# The shape of an array is the number of elements in each dimension.
# By reshaping we can add or remove dimensions or change number of elements in each dimension.

# Reshape From 1-D to 2-D
# Example
# Convert the following 1-D array with 12 elements into a 2-D array.
# The outermost dimension will have 4 arrays, each with 3 elements:


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)

# Reshape From 1-D to 3-D
# Example
# Convert the following 1-D array with 12 elements into a 3-D array.
# The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements:

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)

# Can We Reshape Into any Shape?
# Yes, as long as the elements required for reshaping are equal in both shapes.
# We can reshape an 8 elements 1D array into 4 elements in 2 rows 2D array but we cannot reshape 
# it into a 3 elements 3 rows 2D array as that would require 3x3 = 9 elements.

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr.reshape(2, 4).base) #[1, 2, 3, 4, 5, 6, 7, 8]

# Unknown Dimension
# You are allowed to have one "unknown" dimension.
# Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.
# Pass -1 as the value, and NumPy will calculate this number for you.
# Convert 1D array with 8 elements to 3D array with 2x2 elements:
#Note: We can not pass -1 to more than one dimension.


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)

# Flattening the arrays
# Flattening array means converting a multidimensional array into a 1D array.
# We can use reshape(-1) to do this.

arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)