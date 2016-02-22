__author__ = 'kruthar'
'''
Triangular, Pentagonal, and Hexagonal
Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n-1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n-1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
'''

from generators import *

tri = triangle()
pent = pentagonal()
hex = hexagonal()

pentagons = [pent.next()]
hexagons = [hex.next()]

count = 0

while count < 3:
    test = tri.next()

    while test > pentagons[-1]:
        pentagons.append(pent.next())

    if test not in pentagons:
        continue

    while test > hexagons[-1]:
        hexagons.append(hex.next())

    if test in hexagons:
        count += 1
        print test