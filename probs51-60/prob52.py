__author__ = 'kruthar'
'''
Permuted Multiples
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''

from functions import *

count = 1

while True:
    if isPermutation(str(count), str(count * 2)) and isPermutation(str(count), str(count * 3)) and isPermutation(str(count), str(count * 4)) and isPermutation(str(count), str(count * 5)) and isPermutation(str(count), str(count * 6)):
        print count
        break
    count += 1