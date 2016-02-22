__author__ = 'kruthar'
'''
10001st Prime
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

from generators import *

count = 0

for p in primes():
    count += 1
    if count == 10001:
        print p
        break