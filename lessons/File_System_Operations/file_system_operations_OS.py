# There is am OS module for interacting with the operating system in python

import os

# the os module is used for navigating the file system of our computer.
# there are manu useful tools in the o module, but there are two functions that are most useful for finding filess

#1. os.listdir('.') .. the '.' refers to current directory

print(os.listdir('./'))
# the above prints out all the files in my current directory

print(os.listdir('../Data'))
# the above prints out all the files in my sub-directory

#with 'listdir' we only see the files and subdirectories under the particulat directory we are looking in .
# We cannot use listdir to automatically search through subdirectories. For this we need to use 'walk', which 'walks'
# through all the subdirectories. And (os.path sub-module) for working with file sin Python, particularly if you are working with many different data files at once.

print(os.path.getsize('../Data'))
print(os.path.getatime('../Data'))
print(os.walk('.'))

# the below works me through all the subdirectories from my root directory
for directory, _, filenames in os.walk('/home/patrick/Documents/Semicolon/Machine Learning/ML Programs/Data_Science_World_Quant_University/File_System_Operations'):
     for filename in filenames:
         print(os.path.join(directory,filename))
#
#
# for directory, _, filenames in os.walk('/home/patrick/Documents/Semicolon/Python/Python Programs'):
#     for filename in filenames:
#         print(os.path.join(directory,filename))
#
# # the above is useful when working with datasets that might be spread out over various sub-directories in a data folder
#
# for directory, _, filenames in os.walk('/home/patrick/Documents'):
#     for filename in filenames:
#         print(os.path.join(directory,filename))
#
# for directory, _, filenames in os.walk('/home/patrick/'):
#     for filename in filenames:
#         print(os.path.join(directory,filename))

# for directory, _, filenames in os.walk('/home/patrick'):
#     print(filenames)
#
# for directory, _, filenames in os.walk('/home'):                print(filenames)

for directory, _, filenames in os.walk('/home/patrick/Documents'):
    print(filenames)