def binarysearch(lists, n):
    lists.sort()
    print(lists)
    if len(lists) < 1:
        return False
    midpoint = len(lists) // 2
    if n > lists[midpoint]:
        if len(lists) // 2 == 1:
            for i in lists:
                if i == n:
                    return True
                else:
                    return False
        else:
            return binarysearch(lists[midpoint+1:], n)
    elif n < lists[midpoint]:
        if len(lists) // 2 == 1:
            for i in lists:
                if i == n:
                    return True
                else:
                    return False
        else:
            return binarysearch(lists[:midpoint], n)
    elif lists[midpoint] == n:
        return True


import random

lists = []
counter = 1
while counter <= 3650:
    lists.append(random.randint(1, 2345))
    counter += 1
print(binarysearch(lists, 56))
