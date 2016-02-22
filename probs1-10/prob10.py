__author__ = 'kruthar'
'''
Summation of Primes
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

from generators import *

sum = 0

for prime in primes(2000000):
    sum += prime

print sum