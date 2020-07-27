class Rational(object):

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __repr__(self):
        return "%d/%d" % (self.numerator, self.denominator)

    def __mul__(self, number):
        if isinstance(number, int):
            return Rational(self.numerator * number.numerator, self.denominator)
        elif isinstance(number, Rational):
            return Rational(self.numerator * number.numerator, self.denominator * number.denominator)
        # or concisely (join the two if statments above together)
        # if isinstance(number, (int, rational)):
        #    return Rational(self.numerator*number.numerator, self.denominator*number.denominator)
        else:
            raise TypeError

        # def __rmul__(self, numbers):
        #     return self.__mul__(numbers)

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


print(Rational(34, 2) * Rational(2, 3))
print(Rational(34, 2) * 2)
# print(Rational 2*(34,2))
