# before we can do much with data, we first need to understand how we can bring it
# into python and export it from python

# python interacts with files on disk using the open and close command. When we open a file on disk, we create a file handle. Which is a varibale that allows us to access and manipulate files

# open - open a file for operation
# close - close a file after operation
# 'r - read a file ~  f.read
# 'w' - write to a file  (overwrite the content of a file) ~ f.write
# 'a' - append a new write to a file (adds to what the content in the file) ~ f.write
# 'w+' write and read
# 'r+' read and write
f = open('./Sampletxt', 'r')
data = f.read()
f.close()

# print(data)

f = open('./Data/Alabamarket_python.txt', 'r')
alaba = f.read()
f.close()
totalCount = 0

for txt in alaba:
    if  txt == 'A':
        totalCount+=1

print(totalCount)


# it is a goof habit to close a file handle once we are done with it.
# so usually we will do it automatically using Pyhton's 'with' keyword
# This is known as a context handler

with open('./Data/Alabamarket_python.txt','r') as f:
    alabaWith = f.read()
# no need to do f.close() again, it has been closed automatically woth the python with  keyword
# print(alabaWith)
    print(f.readlines())
# We can read individual lines in a file by using the .readline()/.readlines() method

#print(alabaWith)


# # WRITE DATA TO FILES

with open('./Sampletxt', 'a') as f:
    f.write('\nI am appending a new line to this file')


# to read a file, it must pre-exist
# but we can write to a new file non-existing. It simply creates a new file

with  open('Data/NewFile.txt', 'w+') as f:
    f.write("This is a new file that was created from the IDE")
    NewFile = f.read()
print(NewFile)


with open('Data/NewFile.txt') as f:
    NewFile = f.read()
print(NewFile)