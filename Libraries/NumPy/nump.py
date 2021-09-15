# NumPy is a Python library.
# NumPy is used for working with arrays.
# NumPy is short for "Numerical Python".
# It also has functions for working in domain of linear algebra, fourier transform, and matrices.
# NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely.
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))
print(np.__version__)
# Why Use NumPy?
# In Python we have lists that serve the purpose of arrays, but they are slow to process.
# NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
# The array object in NumPy is called ndarray, it provides a lot of supporting functions that 
# make working with ndarray very easy.
# Arrays are very frequently used in data science, where speed and resources are very important
# The following are the main reasons behind the fast speed of Numpy.
# Numpy array is a collection of similar data-types that are densely packed in memory. APython list can have 
# different data-types, which puts lots of extra constraints while doing computation on it.
# Numpy is able to divide a task into multiple subtasks and process them parallelly.
# Numpy functions are implemented in C. Which again makes it faster compared to Python Lists.