__author__ = 'kruthar'
'''
Square root Digital Expansion
It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.
'''

from functions import *

sum = 0

for i in range(1, 100):
    if math.floor(math.sqrt(i)) ** 2 != i:
        dec = manualSquare(i, 100).replace('.', '')[:100]
        sum += sumList(map(int, dec))

print sum