import numpy as np
# performing mathematical computation with umPy array
# wec can perfomr some uncinvential array calcutions with numpy. Most of these calculations are not possible with lists
a = np.array ([1,2,3,4,5,6])

# direct scalar calcualtions with array
print(a+5)
print(a*5)
print(a/5)
b = a+1
print(b)
print(a/b.astype(float)) # divide two arrays element wise

#linear algebra with numPy array

print(np.dot(a,b)) # inner product of two arrays
print(np.outer(a,b)) # outer product of two arrays

# Universal Functions

# NumPy defines 'ufunc' which allows it to efficiently run functions over arrays. Many of these functions are built
# in, such as np.cos, and implemented in highly performance compiled 'C code'. These functions can perform
# broadcasting which allows them to automatically handle operations between arrays of different shapes, for example
# two arrays with the same shape, or an array and a scalar

#BASIC DATA AGGREGATION

# NumPy's random submodule to create some 'fake data'. Simulating data is useful for testing and prototyping new techniques or code and some algorithms even require random input

np.random.seed(42)
# aggregating data in numPy is a "many-to-one" operation, menaing for several inputs, we get one output or fewer outputs
# for example if we calculate a statistics like mean or variance, thst is a data aggregation. Becuase we are taking a collection of numbers and summarising them with one or fewer numbers

# aside generating randome numbers with numPy random module , we can do random sampling from pre-existing collection of numbers usig submodules shuffle(x) & permutations(x)

jan_coffee_sales = np.random.randint(25, 200, size=(4,7))

print('jan_coffee_sales', end='\n')
print(jan_coffee_sales)


print('Data Aggregation', end='\n\n')

# mean sales
print('Mean Coffees sold per day in January: {}'.format(jan_coffee_sales.mean()), end='\n\n')

# means sales for monday
print('Mean coffees sold on Monday in january {}'.format(jan_coffee_sales[: 1].mean()), end='\n\n')

# days with most sales
print("Days with highest sales was January {}".format(jan_coffee_sales.argmax()+1), end='\n\n')

# days with most salses calculated with python list

jan_coffee_sales_list = jan_coffee_sales.ravel().tolist()

print(jan_coffee_sales_list.index(max(jan_coffee_sales_list))+1)


# MORE COMPLEX CALCULATION

# calculating periodicity of sales - Time Series Analysis
from fractions import Fraction

normalized_sales = (jan_coffee_sales - jan_coffee_sales.mean()) / abs(jan_coffee_sales-jan_coffee_sales.mean())
frequecies = [Fraction.from_float(f).limit_denominator() for f in np.fft.fftfreq(normalized_sales.size)]
power = np.abs(np.fft.fft(normalized_sales.ravel()))**2
xyz = list(zip(frequecies, power))[:len(power) // 2]

print(xyz, end='\n')

# SLicing by condition in numPy

#1. normal slicing

x = np.array(np.random.randint(10, 50, 100))
print(x)
print(x[::2])
print([n for n in x if n%2==0])

# 2. Conditional slicing/filtering
y=(x%2==0)
print(y)

# multiple indexing - not possible with normal python list
# note the double brackets
print(x[[2,3,4,5,6,10]])