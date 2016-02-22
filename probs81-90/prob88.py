__author__ = 'kruthar'
'''
Product-Sum Numbers
A natural number, N, that can be written as the sum and product of a given set of at least two natural numbers,
{a1, a2, ... , ak} is called a product-sum number: N = a1 + a2 + ... + ak = a1 x a2 x ... x ak.

For example, 6 = 1 + 2 + 3 = 1 x 2 x 3.

For a given set of size, k, we shall call the smallest N with this property a minimal product-sum number.
The minimal product-sum numbers for sets of size, k = 2, 3, 4, 5, and 6 are as follows.

k=2: 4 = 2 x 2 = 2 + 2
k=3: 6 = 1 x 2 x 3 = 1 + 2 + 3
k=4: 8 = 1 x 1 x 2 x 4 = 1 + 1 + 2 + 4
k=5: 8 = 1 x 1 x 2 x 2 x 2 = 1 + 1 + 2 + 2 + 2
k=6: 12 = 1 x 1 x 1 x 1 x 2 x 6 = 1 + 1 + 1 + 1 + 2 + 6

Hence for 2<=k<=6, the sum of all the minimal product-sum numbers is 4+6+8+12 = 30; note that 8 is only counted once in the sum.

In fact, as the complete set of minimal product-sum numbers for 2<=k<=12 is {4, 6, 8, 12, 15, 16}, the sum is 61.

What is the sum of all the minimal product-sum numbers for 2<=k<=12000?
'''

from functions import *
import sys

result = dict()
i = 4
limit = 12000
burn = dict()

for a in range(2, limit + 1):
    burn[a] = True

while len(burn) > 0:
    if not isPrime(i):
        for grouping in getMultiplicationGroups(i):
            if len(grouping) < 2:
                continue

            k = i - sumList(grouping) + len(grouping)

            if not result.has_key(k):
                if k <= limit:
                    result[k] = grouping
                    burn.pop(k, None)

    i += 1


sum = 0
prodsums = []

#for k, v in result.iteritems():
#    print str(k) + ": " + str(prodList(v)), v


for z in range(2, limit + 1):
    if result.has_key(z):
        if prodList(result[z]) not in prodsums:
            prodsums.append(prodList(result[z]))
            sum += prodList(result[z])
    else:
        print z

print sum


