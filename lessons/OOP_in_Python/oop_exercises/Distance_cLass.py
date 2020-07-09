#  Exercise 4: Distance
# Another quantity we might want to compute is the distance between two points.
# This is generally given for points $P_1=(x_1,y_1)$ and $P_2=(x_2,y_2)$ as
# $$D = |P_2 - P_1| =   \sqrt{(x_1-x_2)^2 + (y_1-y_2)^2}.$$
#
# Implement a method called `distance` which finds the distance from a point to another point.


import math


class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point(%s, %s)" % (self.x, self.y)

    def distance(self, other):
        return math.sqrt(((self.x - other.x) ** 2) + ((self.y - other.y) ** 2))


point1 = Point(15, 46)
point2 = Point(13, 24)


print(point1.distance(point2))