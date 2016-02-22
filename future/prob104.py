__author__ = 'kruthar'
'''
Pandigital Fibonacci Ends
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.
It turns out that F541, which contains 113 digits, is the first Fibonacci number for which the last nine digits are 1-9 pandigital (contain all the digits 1 to 9, but not necessarily in order). And F2749, which contains 575 digits, is the first Fibonacci number for which the first nine digits are 1-9 pandigital.

Given that Fk is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find k.
'''

from generators import *

count = 1

for fib in fibonacci():
    count += 1
    if isPandigital(str(fib % 1000000000)):
        f = str(fib)
        if isPandigital(f[0:9]):
            print count
            break