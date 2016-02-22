__author__ = 'kruthar'
'''
Sum Square Difference
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 285 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

from generators import *

numsum = 0
prodsum = 0
limit = 100

for a in numbers(limit + 1):
    numsum += a
    prodsum += a ** 2

print numsum ** 2 - prodsum;