# ## Exercise 3: multiplication
#
# Within linear algebra there's many different kinds of multiplication: scalar multiplication, inner product,
# cross product, and matrix product. We're going to implement scalar multiplication and the inner product.
# We can define scalar multiplication given a point $P$ and a scalar $a$ as
#                           𝑎𝑃=𝑎(𝑥,𝑦)=(𝑎𝑥,𝑎𝑦)
#
# and we can define the inner product for points $P,Q$ as
#                       𝑃⋅𝑄=(𝑥1,𝑦1)⋅(𝑥2,𝑦2)=𝑥1𝑥2+𝑦1𝑦2
#
# To test that you've implemented this correctly, compute 2(𝑥,𝑦)⋅(𝑥,𝑦) for a `Point` object. Once this is
# done, execute the `grader.score` cell for this question (do not edit that cell; you only need to modify the `Point`
# class.)
#
# (Remember that `__mul__` method will allow us to use the `*` operator. Also don't forget that the ordering of
# operands matters when implementing these operators.)

class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point(%s, %s)" % (self.x, self.y)

    def __mul__(self, other, scalar=False):
        if isinstance(other, (float, int)):
            return (self.x * other) + (self.y * other)
        elif isinstance(other, Point):
            return (self.x * other.x) + (self.y * other.y)

    def distance(self, center):
        pass


point0 = Point(1, 0)
point1 = Point(-1, 0)

print(point0 * point1)
