__author__ = 'kruthar'

import math
from functions import *

def triangle(limit = None):
    current = 1
    count = 2

    while limit == None or current < limit:
        yield current
        current = (count * (count + 1)) / 2
        count += 1

def square(limit = None):
    current = 1
    count = 2

    while limit == None or current < limit:
        yield current
        current = count ** 2
        count += 1

def squareOfLength(length):
    current = 1
    count = 2

    while len(str(current)) <= length:
        if len(str(current)) == length:
            yield current
        current = count ** 2
        count += 1

def pentagonal(limit = None):
    current = 1
    count = 2

    while limit == None or current < limit:
        yield current
        current = (count * (3 * count - 1)) / 2
        count += 1

def generalizedPentagonal(limit = None):
    current = 1
    count = 1

    while limit == None or current < limit:
        current = (count * (3 * count - 1)) / 2
        yield current
        current = (-count * (3 * -count - 1)) / 2
        yield current
        count += 1

def hexagonal(limit = None):
    current = 1
    count = 2

    while limit == None or current < limit:
        yield current
        current = count * (2 * count - 1)
        count += 1

def heptagonal(limit = None):
    current = 1
    count = 2

    while limit == None or current < limit:
        yield current
        current = (count * (5 * count - 3)) / 2
        count += 1

def octagonal(limit = None):
    current = 1
    count = 2

    while limit == None or current < limit:
        yield current
        current = count * (3 * count - 2)
        count += 1

def numbers(limit = None):
    current = 1

    while limit == None or current < limit:
        yield current
        current += 1

def fibonacci(limit = None):
    fib1 = 0
    fib2 = 1
    fib3 = 1

    while limit == None or fib2 < limit:
        yield fib3
        fib1 = fib2 + fib3
        yield fib1
        fib2 = fib3 + fib1
        yield fib2
        fib3 = fib1 + fib2

def fibstring(limit = None):
    lstring = str(limit)
    fib1 = '1'
    fib2 = '1'

    while limit == None or fib2 < lstring:
        next = ''
        remainder = 0

ps = [3]
def primes(limit = None):
    current = 3
    index = 0

    yield 2
    while limit == None or current < limit:
        yield current

        if index < len(ps) - 1:
            index += 1
            current = ps[index]
        else:
            isPrime = False

            while not isPrime:
                isPrime = True
                current += 2
                sqrt = int(math.sqrt(current))

                for p in ps:
                    if p <= sqrt:
                        if current % p == 0:
                            isPrime = False
                            break
                    else:
                        break
            index += 1
            ps.append(current)

def collatz(start):
    current = start
    while current > 1:
        yield current

        if current % 2 == 0:
            current /= 2
        else:
            current = 3 * current + 1
    yield 1

def abundant(limit = None):
    current = 1
    while limit == None or current < limit:
        while not isAbundant(current):
            current += 1
        yield current
        current += 1

def permutations(list, base = []):
    if len(list) == 1:
        yield base + list

    for a in range(0, len(list)):
        for perm in permutations(list[0:a] + list[a + 1:], base + [list[a]]):
            yield perm

def palindrome(limit = None):
    current = 1

    while limit == None or current < limit:
        while not isPalindrome(str(current)):
            current += 1
        yield current
        current += 1

def starPerms(limit = None):
    current = '1'

    while limit == None or len(current) <= limit:
        inc = True
        for a in reversed(range(len(current))):
            if not inc:
                break

            inc = False
            if current[a] == '*':
                inc = True
                current = current[0:a] + '0' + current[a + 1:]
            elif current[a] == '9':
                current = current[0:a] + '*' + current[a + 1:]
            else:
                current = current[0:a] + str(int(current[a]) + 1) + current[a + 1:]

        if inc:
            current = '1' + current

        if '*' in current:
            yield current

