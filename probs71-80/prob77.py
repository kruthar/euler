__author__ = 'kruthar'
'''
Prime Summations
It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five thousand different ways?
'''

from generators import *

remCounts = dict()

def countSummations(n, last, rem):
    if rem == 0:
        return 1
    if remCounts.has_key(str(last) + ' ' + str(rem)):
        return remCounts[str(last) + ' ' + str(rem)]

    count = 0
    for i in primes(rem + 1):
        if i >= last and i <= rem:
            count += countSummations(n, i, rem - i)

    remCounts[str(last) + ' ' + str(rem)] = count
    return count

n = 2
while True:
    if countSummations(n, 1, n) > 5000:
        print n
        break
    n += 1