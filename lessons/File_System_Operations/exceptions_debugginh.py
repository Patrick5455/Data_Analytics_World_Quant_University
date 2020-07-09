# ask for forgiveness not permission approach

def add(x, y):
    try:
        return x + y
    except TypeError:
        return float(x) + float(y)

# print(add(4,3))


# look before you leap approach

def add_2(x, y):
    if not isinstance(x, (float, int)):
        x = float(x)
    if not isinstance(y, (float, int)):
        y = float(y)
    return x + y

# print(add_2(2,3.6))
