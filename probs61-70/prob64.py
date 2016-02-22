__author__ = 'kruthar'
'''
Odd period square roots
All square roots are periodic when written as continued fractions and can be written in the form:


It can be seen that the sequence is repeating. For conciseness, we use the notation sqrt 23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats indefinitely.

The first ten continued fraction representations of (irrational) square roots are:

sqrt 2=[1;(2)], period=1
sqrt 3=[1;(1,2)], period=2
sqrt 5=[2;(4)], period=1
sqrt 6=[2;(2,4)], period=2
sqrt 7=[2;(1,1,1,4)], period=4
sqrt 8=[2;(1,4)], period=2
sqrt 10=[3;(6)], period=1
sqrt 11=[3;(3,6)], period=2
sqrt 12= [3;(2,6)], period=2
sqrt 13=[3;(1,1,1,1,6)], period=5

Exactly four continued fractions, for N <= 13, have an odd period.

How many continued fractions for N <= 10000 have an odd period?
'''

from functions import *

def getReciprocalCycleFromContinuedFraction(denom):
    prec = 100
    cf = getContinuedFraction(denom, prec)
    list = cf['list']
    reciprocal = dict()

    for i in range(0, len(list)):
        for j in range(i + 1, len(list)):
            if list[i] == list[j]:
                like = True
                k = j
                reps = 0
                while reps == 0:
                    while k + (j - i) < prec:
                        reps += 1
                        if list[i:j] != list[k:k + j - i]:
                            like = False
                            break
                        k += j - i
                    if reps == 0:
                        prec *= 2
                        cf = getContinuedFraction(denom, prec, cf)
                        list = cf['list']

                if like and reps > 0:
                    reciprocal['base'] = list[0:i]
                    reciprocal['cycle'] = list[i:j]
                    return reciprocal

    reciprocal['base'] = ''.join(map(str, list))
    reciprocal['cycle'] = ''
    return reciprocal


limit = 10000
count = 2
odds = 0
square = 2

while count <= limit:
    if count == square ** 2:
        square += 1
        count += 1
        continue
    if len(getReciprocalCycleFromContinuedFraction(count)['cycle']) % 2 != 0:
        print count
        odds += 1
    count += 1

print odds


