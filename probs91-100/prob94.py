__author__ = 'kruthar'
'''
Almost Equilateral Triangles
It is easily proved that no equilateral triangle exists with integral length sides and integral area. However, the almost equilateral triangle 5-5-6 has an area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose perimeters do not exceed one billion (1,000,000,000).
'''

from generators import *

limit = 1000000000
sum = 0

m = 1
m2 = m ** 2
while m2 * 3 + 1 <= limit:
    n = 1
    n2 = n ** 2
    while m2 > n2 and (m2 + n2) * 3 + 1 <= limit:
        a = m2 - n2
        b = 2 * m * n
        c = m2 + n2

        if abs(c - 2 * a) == 1:
            print a, b, c, 2 * c + 2 * a
            sum += 2 * c + 2 * a
        if abs(c - 2 * b) == 1:
            print a, b, c, 2 * c + 2 * b
            sum += 2 * c + 2 * b

        n += 1
        n2 = n ** 2
    m += 1
    m2 = m ** 2

print sum