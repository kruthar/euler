__author__ = 'kruthar'
'''
Prime Power Triples
The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact, there are exactly four numbers below fifty that can be expressed in such a way:

28 = 2^2 + 2^3 + 2^4
33 = 3^2 + 2^3 + 2^4
49 = 5^2 + 2^3 + 2^4
47 = 2^2 + 3^3 + 2^4

How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?
'''

from generators import *

limit = 50000000

pgen = primes()
primes = [pgen.next()]
size = 1
x = 0
triples = dict()
while primes[x] ** 2 < limit:
    x2 = primes[x] ** 2
    y = 0
    while x2 + primes[y] ** 3 < limit:
        y3 = primes[y] ** 3
        z = 0
        while x2 + y3 + primes[z] ** 4 < limit:
            z4 = primes[z] ** 4
            if z == size - 1:
                size *= 2
                while len(primes) < size:
                    primes.append(pgen.next())
            triples[x2 + y3 + z4] = True
            z += 1
        if y == size - 1:
            size *= 2
            while len(primes) < size:
                primes.append(pgen.next())
        y += 1
    if x == size - 1:
        size *= 2
        while len(primes) < size:
            primes.append(pgen.next())
    x += 1

print len(triples.keys())
