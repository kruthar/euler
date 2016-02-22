__author__ = 'kruthar'
'''
Diophantine Equation
Consider quadratic Diophantine equations of the form:

x^2 - Dy^2 = 1

For example, when D=13, the minimal solution in x is 649^2 - 13x180^2 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

3^2 - 2x2^2 = 1
2^2 - 3x1^2 = 1
9^2 - 5x4^2 = 1
5^2 - 6x2^2 = 1
8^2 - 7x3^2 = 1

Hence, by considering minimal solutions in x for D <= 7, the largest x is obtained when D=5.

Find the value of D <= 1000 in minimal solutions of x for which the largest value of x is obtained.
'''

from functions import *

def getDiophantine(d):
   prec = 10
   cf = getContinuedFraction(d, prec)
   simp = simplifyContinuedFraction(cf)
   current = 1

   while True:
       if current >= len(simp):
           prec *= 2
           cf = getContinuedFraction(d, prec, cf)
           simp = simplifyContinuedFraction(cf, simp)

       if simp[current]['numer'] ** 2 - d * simp[current]['denom'] ** 2 == 1:
           return {'x': simp[current]['numer'], 'y': simp[current]['denom']}
       current += 1


square = 2
current = 2
max = 0
maxx = 0
limit = 1000
while current <= limit:
    print current
    if current == square ** 2:
        square += 1
        current += 1
        continue

    dx = getDiophantine(current)['x']
    if dx > max:
        max = dx
        maxx = current

    current += 1

print max
print maxx
