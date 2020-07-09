## Exercise 1:
# `point_repr` The first step in defining most classes is to define their `__init__` and `__repr__`
# methods so that we can construct and represent distinct objects of that class. Our `Point` class should accept two
# arguments, `x` and `y`, and be represented by a string `'Point(x, y)'` with appropriate values for `x` and `y`.
#  When you've written a `Point` class capable of this, execute the cell with `grader.score` for this question (do not
# edit that cell; you only need to modify the `Point` class).

class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point(%s, %s)" % (self.x, self.y)

print(Point(3,4))