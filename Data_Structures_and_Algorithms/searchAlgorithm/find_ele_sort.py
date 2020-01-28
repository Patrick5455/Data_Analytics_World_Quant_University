# The goal of the algorithms in this package is to test for Time Complexity.
# This is the sorting  algorithm (second fastest) and it is 0(N)
def find_ele_sort(list_, ele):
    for n in list_:
        if n == ele:
            return True
        if n > ele:
            return False
    else:
        False


import random

n = 50
lispt = []
counter = 0
while counter <= n:
    lisp = random.randint(1, n)
    lispt.append(lisp)
    counter += 1
# The algorithm requires a sorted list
lispt.sort()
sing = random.randint(1, n)
print(lispt)
print(sing)
print(find_ele_sort(lispt, sing))
