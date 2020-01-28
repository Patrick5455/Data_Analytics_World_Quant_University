class Rectangle(object):

    def __init__(self, height, length):
        self.height = height
        self.length = length

    def __repr__(self):
        return self.height, self.length

    def area(self):
        return self.height * self.length

    def perimetre(self):
        return 2 * (self.length + self.height)


rec1 = Rectangle(2, 4)
print(rec1.area())
print(rec1.perimetre())


# Inheritance
class Square(Rectangle):
    def __init__(self, length):
        # Super Class
        super(Square, self).__init__(length, length)  # Or Rectangle.__init__(length, length)

    # Remodify an existing function from the superclass for additional funtionality
    def area(self):
        print("Computing Area")
        return Rectangle.area(self) # Or super(Square, self).area()



sqr1 = Square(2)
print(sqr1.area())

# Hence:
print(isinstance(sqr1, Rectangle))
print(type(sqr1) == Rectangle)
print(type(sqr1) == Square)
