# compared to a list , arrays are much more less flexible
# jnumPy arrays are stored in a contiguous block of memory and every element use a uniformed amount of memory. unlike python lists that takes more unnecessary space
# numPy arrays are implemented not in python but in C. THis allows for very fast iteratin in the array.
# another advanatge of the uniformed array, is that every element of the array have a unifored mathematical behaviour hence in numPy, there is noe check wthere containing elements agree in the mathematical operation. This leds us to do calcualtion more qucikl because we dont do a check first unlike a list.
import timeit

import numpy as np

time_list = [np.random.random() for _ in range(1000000)]

time_arr = np.array(time_list)

print(time_list[:5])

timeit

sum(time_list)

print(timeit, np.sum(time_arr))

# summing list of lists can be complex but it is simpler in numPy array

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

an_array = np.array(list_of_lists)

# summing list_of_lists in python
print(sum([sum(inner_list) for inner_list in list_of_lists]))

# summing multi-dimensaion array in python
print(an_array.sum())

# summing rows

# inner list in python
print([sum(inner_list) for inner_list in list_of_lists])

# numPy array
print(an_array.sum(axis=1))  # axis 1 in numPy array is a row

# summing column in  python lists
print('nested sum to sum list of lists column', end='\n')
x = [sum(row[index] for row in list_of_lists) for index in range(len(list_of_lists[0]))]
print(x)

print('straightforward sum for numPy array column sum', end='\n')
y = an_array.sum(axis=0)
print(y)

# numPy is the basic for many ither data science packages
