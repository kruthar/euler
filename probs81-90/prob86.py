__author__ = 'kruthar'
'''
Cuboid Route
A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly, F, sits in the opposite corner.
By travelling on the surfaces of the room the shortest "straight line" distance from S to F is 10 and the path is shown on the diagram.

However, there are up to three "shortest" path candidates for any given cuboid and the shortest route doesn't always have integer length.

It can be shown that there are exactly 2060 distinct cuboids, ignoring rotations, with integer dimensions, up to a maximum
size of M by M by M, for which the shortest route has integer length when M = 100. This is the least value of M for which
the number of solutions first exceeds two thousand; the number of solutions when M = 99 is 1975.

Find the least value of M such that the number of solutions first exceeds one million.
'''

import math
import sys

squares = dict()

def isSquare(n):
    if not squares.has_key(n):
        root = math.sqrt(n)
        squares[n] = root == int(root)
    return squares[n]

limit = 1000000
a = 1
count = 0

# You can find the candidate shortest paths from catty cornor points in a cuboid room by doing the pythagorean theorem
# for one side and the sum of the other two sides, that leaves three possible routes. Imagine folding the cuboid flat
# like a piece of paper.

# Research showed that if you  ordered the sides largest to smallest, then the biggest side would always be the lone side
# in the equation. EX. for the cuboid 3 x 5 x 6 the shortest route can be found with sqrt(6^2 + (3 + 5)^2).

# a triple nested approach was too slow, so you can just use a double nested and infer how many possible cuboids you would
# have when you find an integer solution for a particular (b + c).

while count < limit:
    a2 = a ** 2
    lim = a * 2
    bc = 2
    while bc <= lim:
        if isSquare(a2 + bc ** 2):
            b = (bc + 1) / 2
            while b <= a and  bc - b >= 1:
                count += 1
                b += 1
        if count > limit:
            print a
            sys.exit()
        bc += 1
    a += 1
