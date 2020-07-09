# The goal of the algorithms in this package is to test for Time Complexity.
# This is the binary search algorithm (fastest) and it is logN(N)
def find_ele_sort_binary(list_, ele):
    # use a sorted list for the algorithm
    if len(list_) < 1:
        return False
    midpoint = len(list_) // 2
    if list_[midpoint] == ele:
        return True
    elif list_[midpoint] > ele:
        return find_ele_sort_binary(list_[:midpoint], ele)
    # elif list_[midpoint] < ele:
    else:
        return find_ele_sort_binary(list_[midpoint+1:], ele)


import random
lispt = []
counter = 0
n = 50
while counter <= n:
    lisp = random.randint(1, n*10)
    lispt.append(lisp)
    counter += 1
# The binary search Algorithm also requires a sorted list
lispt.sort()
print(lispt)
lis = random.randint(1, n*10)
print(lis)
print(find_ele_sort_binary(lispt, lis))




