# Access Array Elements
# Array indexing is the same as accessing an array element.
# You can access an array element by referring to its index number.
# The indexes in NumPy arrays start with 0, meaning that the first element has index 0, and the second 
# has index 1 etc.
import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr[2] + arr[3])

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('4th element on 1st dim: ', arr[0, 3])

# Access 3-D Arrays
# To access elements from 3-D arrays we can use comma separated integers representing the 
# dimensions and the index of the element.
# Access the third element of the second array of the first array:
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])

# [
#     [
#         [1, 2, 3], [4, 5, 6]
#     ], 
#     [
#         [7, 8, 9], [10, 11, 12]
#     ]
# ]


# Negative Indexing
# Use negative indexing to access an array from the end.
# Print the last element from the 2nd dim:

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -1])