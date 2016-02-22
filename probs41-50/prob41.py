__author__ = 'kruthar'
'''
Pandigital Prime

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''

from generators import *

max = 0

for prime in primes(1000000000):
    if isPandigital(str(prime)):
        max = prime
    print prime

print max