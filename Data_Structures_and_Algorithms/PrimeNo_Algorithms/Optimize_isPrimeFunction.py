# Unoptimised function
def is_prime(number):
    if number <= 1:
        return False
    for factor in range(2, number):
        if number % factor == 0:
            return False
    return True


# Optimised Function
import math


def is_prime_fast(n):
    nroot = int(math.sqrt(n))
    # print(nroot)
    if n < 1:
        return False
    if n % 2 == 0 and n > 2:
        return False
    else:
        for f in range(2, nroot + 1):
            # print(f)
            if f % 2 != 0 and n % f == 0:
                return False
    return True
