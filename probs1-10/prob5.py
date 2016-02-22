__author__ = 'kruthar'
'''
Smallest Multiple
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

from functions import *
from generators import *

list = []

for a in numbers(21):
    list.append(a)

multiples = smallestMultiple(list)

product = 1
for key, value in multiples.iteritems():
    for i in range(value):
        product *= key

print product