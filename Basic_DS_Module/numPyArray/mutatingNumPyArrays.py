# Changing shape. Often we will want ot take arrays that are one shape and transform them to a different shape more
# amenable to a specific condition

import numpy as np

an_array = np.random.randint(12, 45, size=(3,3))
print(an_array)

#print(an_array.shape )

# changing the shape of an array

## not working - work in progress
reshaped_array = an_array.shape = (9,1)

# .ravel is used to unravel an array into one dimension

x = an_array.ravel()
print(x)

y=an_array.ravel().shape  # returns the shape of the unravel array

# - transpose shape of array

y=an_array.transpose()

print(y, end='Transpose reshpaing')

# stcking array

b = an_array*5
print(b)

#  stakcing

print(np.hstack((an_array, b)))
print(np.vstack((an_array, b)))
print(np.dstack((an_array, b)))