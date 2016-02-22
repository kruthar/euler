__author__ = 'kruthar'
'''
Prime Pair Sets
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the
result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes,
792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
'''

from generators import *
from functions import *

limit = 5
pairs = dict()
found = False

def putInto(x, y):
    if pairs.has_key(y):
        if x not in pairs[y]:
            pairs[y].append(x)
    else:
        pairs[y] = [x]

def check(x):
    possibles = pairs[x][:] + [x]

    while True:
        # if our possibles list is less then limit then a solution is impossible
        if len(possibles) < limit:
            return []

        temp = [x]

        # for each remaining pair in the possibles list make a list of intersections with the possible list itself
        for pair in possibles:
            if pair == x:
                continue

            intersections = [pair]
            for item in pairs[pair]:
                if item in possibles:
                    intersections.append(item)

            # if the intersection list is less then the limit then this pair cannot be in the solution
            if len(intersections) >= limit:
                temp.append(pair)

        last = len(possibles)
        possibles = temp[:]

        # end when we make no more progress
        if len(possibles) == last:
            break

    if len(possibles) == limit:
        return possibles

    return []

count = 0
bound = 1000
pgen1 = primes()
ps = []

while not found:
    current = pgen1.next()
    p1 = str(current)

    for a in ps:
        p2 = str(a)
        if isPrime(int(p1 + p2)) and isPrime(int(p2 + p1)):
            #print p1 + ' ' + p2 + ' ' + p2 + p1
            putInto(p1, p2)
            putInto(p2, p1)
            temp = check(p1)
            if len(temp) >= limit:
                print temp
                print sumList(map(int, temp))
                found = True
                break
            temp = check(p2)
            if len(temp) >= limit:
                print temp
                print sumList(map(int, temp))
                found = True
                break
        pass

    ps.append(current)