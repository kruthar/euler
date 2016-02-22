__author__ = 'kruthar'
'''
Cubic Permutations
The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3).
In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
'''

from functions import *
from generators import *

magnitude = 0
limit = 5
cubes = [0]

def update(mag):
    stop = 10 ** mag
    perms = dict()

    while len(cubes) ** 3 < stop:
        cube = len(cubes) ** 3
        cubes.append(cube)
        s = ''.join(sorted(str(cube)))
        if perms.has_key(s):
            perms[s].append(cube)
        else:
            perms[s] = [cube]

    least = -1

    for list in perms.itervalues():
        if len(list) == limit:
            if min(list) < least or least < 0:
                least = min(list)

    return least

result = -1

while result < 0:
    magnitude += 1
    result = update(magnitude)

print result
