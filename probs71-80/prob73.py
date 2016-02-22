__author__ = 'kruthar'
'''
Counting Fractions in a range
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d <= 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d <= 12,000?
'''

from functions import *

limit = 12000

denom = 2
count = 0
above = 1.0/2
below = 1.0/3

while denom <= limit:
    print denom
    numer = int(denom * below) - 1
    while True:
        value = float(numer) / denom
        if value >= above:
            break
        if value > below and (isPrime(denom) or relativelyPrime(numer, denom)):
            count += 1
        numer += 1
    denom += 1

print count