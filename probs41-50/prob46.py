__author__ = 'kruthar'
'''
Goldbach's other conjecture
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2x1^2
15 = 7 + 2x2^2
21 = 3 + 2x3^2
25 = 7 + 2x3^2
27 = 19 + 2x2^2
33 = 31 + 2x1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''

from generators import *

p = primes()
primes = [p.next()]
found = True
count = 7
while found:
    count += 2
    if isPrime(count):
        continue

    found = False

    while count > primes[-1]:
        primes.append(p.next())

    for prime in primes:
        test = 1
        while count - prime >= 2 * test ** 2:
            if count == prime + 2 * test ** 2:
                found = True
                break
            test += 1

        if found:
            break

print count
