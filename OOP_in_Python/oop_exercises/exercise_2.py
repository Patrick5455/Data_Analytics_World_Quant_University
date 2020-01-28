# ## Exercise 2: add_subtract

# The most basic vector operations we want our `Point` object to handle are addition and subtraction. For two points
# $(x_1, y_1) + (x_2, y_2) = (x_1 + x_2, y_1 + y_2)$ and similarly for subtraction. Implement a method within `Point`
# that allows two `Point` objects to be added together using the `+` operator, and likewise for subtraction. Once
# this is done, execute the `grader.score` cell for this question (do not edit that cell; you only need to modify the
# `Point` class.)
# (Remember that `__add__` and `__sub__` methods will allow us to use the `+` and `-` operators.)

class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point(%s, %s)" % (self.x, self.y)

    def __add__(self, another_point):
        return Point(self.x + another_point.x, self.y + another_point.y)

    def __sub__(self, another_point):
        return Point(self.x - another_point.x, self.y - another_point.y)


point1 = Point(3, 4)
point2 = Point(5, 6)

print((point1 + point2))
print((point1 - point2))
