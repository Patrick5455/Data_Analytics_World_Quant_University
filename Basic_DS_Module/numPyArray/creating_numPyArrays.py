import numpy as np

list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]

# Aside contructing an array by passing an aray into numpy.array, we can do generate our arrays with numPy
# numPy provides a number of conveninet functions for generating array of different forms.

x=np.linspace(1,10,10) # linearly spaced points.
print(x, end='\n\n')
x=np.linspace(0,10,5) # linspae is inclusive of the upperbound. so we have to be very careful if we don't want some particular values.
print(x, end='\n\n')

y = np.arange(1, 10, 1)
print(y, end='\n\n')

y = np.array(range(1,10)) # python range function; pass the generator to np.array
print(y, end='\n\n')

#logarithmically spaced points
z = np.logspace(1,10, 10)
print(z, end='\n\n')

#multidiensinal arrays

a = np.zeros((10, 2,  5))
print(a, end='\n\n')
a = np.zeros((5, 10, 2))
print(a, end='\n\n')

#diagonal arrays = diagonal matrix
b = np.diag([1,2,3,4])
print(b, end='\n\n')

b = np.eye(5)
print(b, end='\n\n')

#numPy is often used for Linear ALgebra

#change the dataType of an array (recast thee dataType of a numPy array)
print(np.logspace(1,10,10))
print(np.logspace(1,10,10).dtype)
print(np.logspace(1,10,10).astype(int))
print(np.logspace(1,10,10).astype(int).dtype)

print(end='\n\n')
print('Casting dataType in numpy, convert boolean to integers')
print(np.array([False, True]).astype(float))