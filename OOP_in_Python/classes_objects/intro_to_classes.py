class Rational(object):

    # Object initialisation and its attributes
    def __init__(self, numerator, denominator):
        # The object it(self) is the first argument in a method of any object.
        # self here refers to the object argument passed into the class declaration
        self.numerator = numerator
        self.denominator = denominator
        # Hence in: More common syntax - ration.reduce() - ration the instance (object) creation of class Rational is
        # implicitly passed into the method call of object ration.
        # The Less common syntax is  - Rational.reduce(ration)
        # - ration, the object (instance of class Rational) is passed into the method call
        # NB: Note that the use of "self" here is "arbitrary". Anything can be used e.g "this" (for java)

    # Object Representation
    def __repr__(self):
        return "%d/%d" % (self.numerator, self.denominator)

    # helper method (methods with single _. Just like private method in java.
    # Even though the "privacy of an helper method is not emphasized in python,
    # it is expected that another programmer does not use it")
    def _gcd(self):
        minNum = min(self.numerator, self.denominator)
        maxNum = max(self.numerator, self.denominator)
        smallest_divisors = {i for i in range(1, minNum + 1) if minNum % 1 == 0}
        common_divisors = {i for i in smallest_divisors if maxNum % i == 0}
        return max(common_divisors)

    def reduce(self) -> object:
        gcd = self._gcd()
        self.numerator = self.numerator / gcd
        self.denominator = self.denominator / gcd
        return self


fraction = Rational(16, 32)
print(fraction)  # Or print(Rational(16, 32))
fraction.reduce()  # Or Rational.reduce(fraction)
print(fraction)
