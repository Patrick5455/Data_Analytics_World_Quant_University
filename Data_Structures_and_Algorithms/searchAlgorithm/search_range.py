# The goal of the algorithms in this package is to test for Time Complexity.
# This is the loop algorithm (slowest) and it is 0(N)
def find_ele(list_, ele):
    for num in list_:
        if num == ele:
            return True
    else:
        return False


import random
counter = 0;
ni = 50
nisps_ = []
while counter < ni:
    nisp = random.randint(1, ni*10)
    nisps_.append(nisp)
    counter += 1
print(nisps_)
ink = random.randint(1, ni * 50)
print(ink)
print(find_ele(nisps_, ink))
