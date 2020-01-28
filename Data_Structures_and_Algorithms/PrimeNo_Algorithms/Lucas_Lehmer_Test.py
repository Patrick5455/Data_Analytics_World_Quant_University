# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 18:08:02 2020

@author: USER
"""


# @Patrick_Ojunde
def is_prime(n):
    if n <= 1:
        return False
    for factor in range(2, n):
        if n % factor == 0:
            return False
    return True


def mersenne_number(n):
    if is_prime(n):
        n = 2 ** n - 1
        return  n

# Test Mersenne_Number
listM = [number for number in range(3, 65) if (mersenne_number(number))]

print(listM)


def lucas_lehmerII(prime):
    lists = [4]
    lucas_series = 4
    index = prime - 2
    mersenne = (2 ** prime) - 1
    for number in range(index):
        lucas_series = (lucas_series ** 2) - 2
        lucas_series = lucas_series % mersenne
        lists.append(lucas_series)
    return lists


print(lucas_lehmerII(5))

"""
For a given Mersenne number with exponent  p , the number is prime if the Lucas-Lehmer series is 0 at position  p−2 . Write a function that tests if a Mersenne number with exponent p is prime. Test if the Mersenne numbers with prime  p  between 3 and 65 (i.e. 3, 5, 7, ..., 61) are prime. Your final answer should be a list of tuples consisting of (Mersenne exponent, 0) (or 1) for each Mersenne number you test, where 0 and 1 are replacements for False and True respectively.
HINT: The zip function is useful for combining two lists into a list of tuples
"""


def ll_prime():
    prime_list = []
    lucas_check = []
    for n in range(3, 65):
        if is_prime(n):
            prime_list.append(n)
    for p in prime_list:
        mersenne = (2 ** p) - 1
        index = p - 2
        lucas_series = 4;
        for _ in range(index):
            lucas_series = (lucas_series ** 2) - 2
            lucas_series = lucas_series % mersenne
        if lucas_series == 0:
            prime_check = 1
        else:
            prime_check = 0
        lucas_check.append(prime_check)
    return list(zip(prime_list, lucas_check))


print(ll_prime())

