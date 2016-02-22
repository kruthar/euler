__author__ = 'kruthar'
'''
Pandigital Products
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''

from generators import *

results = dict()
sum = 0

for perm in permutations([1,2,3,4,5,6,7,8,9]):
    for a in range(1, 8):
        b = 0
        while a + b <= 7:
            x = int(''.join(map(str, perm[0:a])))
            y = int(''.join(map(str, perm[a:b + a + 1])))
            z = int(''.join(map(str, perm[a + b + 1:])))

            if x * y == z:
                print '%d * %d = %d %d %d %d' % (x, y, z, int(''.join(map(str, perm))), a, b)
                results[z] = True
            b += 1

for prod in results.iterkeys():
    print prod
    sum += prod
print sum