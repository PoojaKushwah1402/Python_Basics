# Slicing in python means taking elements from one given index to another given index.
# We pass slice instead of index like this: [start:end].
# We can also define the step, like this: [start:end:step].
# If we don't pass start its considered 0
# If we don't pass end its considered length of array in that dimension
# If we don't pass step its considered 1
# Slice elements from index 1 to index 5 from the following array:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

# Negative Slicing
# Use the minus operator to refer to an index from the end:
# Slice from the index 3 from the end to index 1 from the end:

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1])

# STEP
# Use the step value to determine the step of the slicing:
# Return every other element from index 1 to index 5:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[:5:3])


# Slicing 2-D Arrays
# From both elements, return index 2:

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 2])