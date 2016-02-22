__author__ = 'kruthar'
'''
The incenter of a triangle
ABC is an integer sided triangle with incenter I and perimeter p.
The segments IA, IB and IC have integral length as well.

Let L = p + |IA| + |IB| + |IC|.

Let S(P) = sigma L for all such triangles where p <= P. For example, S(10^3) = 3619.

Find S(10^7).
'''

from functions import *

limit = 10000

def heronian():
    m = 1
    divisors = getDivisors(m)
    while m < 20:
        for n in range(1, m + 1):
            if gcd([m, n]) != 1:
                continue
            for k in range(max(1, int(math.floor(math.sqrt(m ** 2 * n / (2 * m + n))))), int(math.ceil(math.sqrt(m * n)))):
                if gcd([m, k]) != 1 or gcd([n, k]) != 1:
                    continue
                a = n * (m ** 2 + k ** 2)
                b = m * (n ** 2 + k ** 2)
                c = (m + n) * (m * n - k ** 2)
                g = gcd([a, b, c])

                print '%d %d %d    %d %d %d' % (a/g, b/g, c/g, m, n, k)

        m += 1
heronian()
