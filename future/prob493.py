__author__ = 'kruthar'
'''
Under the Rainbow
70 colored balls are placed in an urn, 10 for each of the seven rainbow colors.

What is the expected number of distinct colors in 20 randomly picked balls?

Give your answer with nine digits after the decimal point (a.bcdefghij).
'''

import math

def numSubsets(subsets, total):
    if subsets == 1:
        if total <= 10 and total > 0:
            return [[total]]
        else:
            return []

    results = []
    for i in range(1, 11):
        if i <= total + 1 - subsets:
            for result in numSubsets(subsets - 1, total - i):
                results.append([i] + result)


    return results

def bruteSets(subsets, m):
    results = []
    for result in bruteSetsHelper(subsets):
        total = 0
        for c in result:
            total += c
        if total == m:
            results.append(result)

    return results


def bruteSetsHelper(subsets):
    if subsets == 0:
        return [[]]

    results = []
    for i in range(1, 11):
        for result in bruteSetsHelper(subsets - 1):
            results.append([i] + result)

    return results

def choose(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))

print len(bruteSets(4, 20))
print len(numSubsets(4, 20))

expected = 0
total = 0
for i in range(2, 8):
    print i, choose(7, i), len(numSubsets(i, 20)), float(choose(7, i)) * len(numSubsets(i, 20))
    temp = float(choose(7, i)) * len(numSubsets(i, 20))
    total += temp
    expected += i * temp

print expected, total, expected / total


