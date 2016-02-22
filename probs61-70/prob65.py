__author__ = 'kruthar'
'''
Convergents of e
The square root of 2 can be written as an infinite continued fraction.

Hence the sequence of the first ten convergents for sqrt 2 are:

1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...
What is most surprising is that the important mathematical constant,
e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

The first ten terms in the sequence of convergents for e are:

2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.
'''

from functions import *

cf = {'base': 2, 'list': []}

limit = 99
current = 1
count = 0

while count < limit:
    if count < limit:
        cf['list'].append(1)
        count += 1
    if count < limit:
        cf['list'].append(2 * current)
        count += 1
    if count < limit:
        cf['list'].append(1)
        count += 1
    current += 1

print sumList(map(int, list(str(simplifyContinuedFraction(cf)[limit]['numer']))))