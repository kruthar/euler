__author__ = 'kruthar'
'''
Consecutive Prime Sum
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''

from generators import *
from functions import *
import itertools

pgen = primes()
sums = dict()
sum = pgen.next()
plist = [sum]
limit = 1000000

while len(plist) > 0:
    if isPrime(sum):
        if not sums.has_key(sum) or sums[sum] < len(plist):
            sums[sum] = len(plist)

    prime = pgen.next()
    if sum + prime < limit:
        sum += prime
        plist.append(prime)
    else:
        popped = plist.pop(0)
        sum -= popped
        pgen = itertools.chain([prime], pgen)

max = 0
maxp = 0

for sum, count in sums.iteritems():
    if count > max:
        max = count
        maxp = sum

print maxp
print max