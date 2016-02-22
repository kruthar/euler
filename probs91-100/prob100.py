__author__ = 'kruthar'
'''
Arranged Probability
If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken
at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)x(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing
eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 10^12 = 1,000,000,000,000 discs in total, determine the number of blue discs that the box would contain.
'''

from functions import *
import time

prec = 50

def solveQuadratic(a, b, c):
    inner = b * b - 4 * a * c
    if inner < 0 or not isSquare(inner):
        return None, None

    sqrtInner = math.sqrt(inner)
    left = (-b - sqrtInner) / (2 * a)
    right = (-b + sqrtInner) / (2 * a)
    return left, right

def findC(total):
    return -(total * total) + total

def findB(total):
    return solveQuadratic(2, -2, findC(total))

start = 10**12

while True:
    left, right = findB(start)
    if right != None:
        print start, right
        break
    start += 1