__author__ = 'kruthar'
'''
Singular Integer Right Triangles
It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, but there are many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one solution to be found;
for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L <= 1,500,000 can exactly one integer sided right angle triangle be formed?
'''

from functions import *
import math

limit = 1500000
m = 2
triangles = dict()
sides = dict()

a = 0
b = 0
c = 0

while m ** 2 + 1 <= limit / 2:
    n = 1
    done = False
    while m > n:
        if (n % 2 == 0 or m % 2 == 0) and relativelyPrime(n, m):
            a = m ** 2 - n ** 2
            b = 2 * m * n
            c = m ** 2 + n ** 2

            p = a + b + c
            x = 1
            while p * x <= limit:
                if not sides.has_key(str(p * x) + ' ' + str(c * x)):
                    if triangles.has_key(p * x):
                        triangles[p * x] += 1
                    else:
                        triangles[p * x] = 1
                    #print 'tried %d %d %d %d %d' % (a * x, b * x, c * x, m, n)
                    sides[str(p * x) + ' ' + str(c * x)] = True
                x += 1
        n += 1

    if done:
        break

    m += 1

print triangles

count = 0
for key, value in triangles.iteritems():
    if value == 1 and key <= limit:
        count += 1

print count