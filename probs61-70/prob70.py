__author__ = 'kruthar'
'''
Totient Permutation
Euler's Totient function, p(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n.
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, p(9)=6.
The number 1 is considered to be relatively prime to every positive number, so p(1)=1.

Interestingly, p(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 10^7, for which p(n) is a permutation of n and the ratio n/p(n) produces a minimum.
'''

from functions import *

limit = 10 ** 7

min = -1
minn = 0

for a in range(3, limit, 2):
    if isPrime(a):
        continue
    t = totient(a)
    prod = float(a) / t
    if isPermutation(str(t), str(a)) and (prod < min or min < 0):
        min = prod
        minn = a

print minn