__author__ = 'kruthar'
'''
Distinct Primes Factors
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 x 7
15 = 3 x 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 x 7 x 23
645 = 3 x 5 x 43
646 = 2 x 17 x 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
'''

from functions import *

test = 4
count = 1
consec = 0

while consec < test:
    pfs = len(primeFactors(count))
    if pfs != test:
       consec = 0
    else:
        consec += 1

    count += 1

print count - test
