# ## Exercise 5: Algorithm
#
# Now we will use these points to solve a real world problem!  We can use our Point objects to represent measurements
# of two different quantities (e.g. a company's stock price and volume).  One thing we might want to do with a data
# set is to separate the points into groups of similar points.  Here we will implement an iterative algorithm to do
# this which will be a specific case of the very general $k$-means clustering algorithm.  The algorithm will require
# us to keep track of two clusters, each of which have a list of points and a center (which is another point,
# not necessarily one of the points we are clustering).  After making an initial guess at the center of the two
# clusters, $C_1$ and $C_2$, the steps proceed as follows
#
# 1. Assign each point to $C_1$ or $C_2$ based on whether the point is closer to the center of $C_1$ or $C_2$.
# 2. Recalculate the center of $C_1$ and $C_2$ based on the contained points.
#
# See [reference](https://en.wikipedia.org/wiki/K-means_clustering#Standard_algorithm) for more information.
#
# This algorithm will terminate in general when the assignments no longer change.  For this question, we would like
# you to initialize one cluster at `(1, 0)` and the other at `(-1, 0)`.
#
# The returned values should be the two centers of the clusters ordered by greatest `x` value.  Please return these
# as a list of numeric tuples $[(x_1, y_1), (x_2, y_2)]$
#
# In order to accomplish this we will create a class called cluster which has two methods besides `__init which you
# will need to write.
# The first method `update` will update the center of the Cluster given the points contained
# in the attribute `points`.  Remember, you after updating the center of the cluster, you will want to reassign the
# points and thus remove previous assignments.  The other method `add_point` will add a point to the `points`
# attribute.
#
# Once this is done, execute the `grader.score` cell for this question (do not edit that cell; you only need to
# modify the `Cluster` class and `compute_result` function.)

# Class Point
import math


class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point(%s, %s)" % (self.x, self.y)

    def distance(self, other):
        if isinstance(other, Point):
            return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


point1 = Point(3, 4)
point2 = Point(13, 24)

point3 = Point(5, 6)
point4 = Point(10, 61)

# print(point1.distance(point2))
# print(point3.distance(point4))

class Cluster(object):
    def __init__(self, x, y):
        self.center = Point(x, y)
        self.point = Point(x, y)
        self.points = []

    # Update the centre of the point
    def update(self):
        sumX = 0
        for i in range(len(self.points)):
            sumX += self.points[i].x

        sumY = 0
        for i in range(len(self.points)):
            sumY += self.points[i].y

        self.center = Point(sumX / len(self.points), sumY / len(self.points))
        self.points = []

    # add a point to a list of points
    def add_point(self, point):
        return self.points.append(point)


def compute_result(points):
    points = [Point(*point) for point in points]
    a = Cluster(1, 0)
    b = Cluster(-1, 0)

    a_old = []
    for _ in range(10000):  # max iterations
        for point in points:
            if point.distance(a.center) < point.distance(b.center):
                a.add_point(point)
            else:
                b.add_point(point)

        if a_old == a.points:
            break

        a_old = a.points
        a.update()
        b.update()
    if a.center.x > b.center.x:
        return [(a.center.x, a.center.y), (b.center.x, b.center.y)]
    else:
        return [(b.center.x, b.center.y), (a.center.x, a.center.y)]

print(compute_result([(2, 2), (4, 78), (0, 0), (-1, -10), (-5, -5)]))
