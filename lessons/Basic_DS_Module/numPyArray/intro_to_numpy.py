# numpy alongside scipy are one of the oldest librarires for data science.
# Numpy offers advamced mathematical functions such as sine,co-sine, logarithm, its random module for random sampling
# A NumPy array is similiar to a mathimaticla n-dimensional array. This is similiar to list of lists in python
# A numPy array could be 2, 3, 4, dimensional array. Such arrays are useful fo representing images, colours, etc.

# A numPy array os highlyoptimised for perforing mathematical calculations

import numpy as np

list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]
print(list_of_lists, end='\n\n')


print("Numpy Array")
an_array = np.array(list_of_lists)
print(an_array)
print(type(an_array))

# A nyumoy array has a shape given by the size of its dimension
#A list of lists can have different lenghts but passing such unequal lenght of lists in a numpy array could become an issue

non_rectangular = [[1,2],[4,5,6],[10, 7,8,9]]

poor_numpy = np.array(non_rectangular)

# notice how the unequal length array is printed when passed to numpy
print(poor_numpy)
#numPy array must be rectangular. It must have the same number of element in each row and the same number of element in each column.

print(end='\n' 'Data type and shape of the two arrrays')
print(end='\n')
print(an_array.shape, an_array.dtype)
print(poor_numpy.shape, poor_numpy.dtype)

# numPy Arrays are ordered, mutable and homogeneous data structures.

