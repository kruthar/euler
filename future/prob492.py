__author__ = 'kruthar'

from generators import *

def multiplyToDigits(ta, tb, digits):
    a = str(max(ta, tb))
    b = str(min(ta, tb))
    product = 0

    i = len(a) - 1
    while i > len(a) - digits - 1 and i >= 0:
        remainder = 0
        agg = '0' * (len(a) - i - 1)
        j = len(b) - 1
        while j > len(b) - digits - 1 and j >= 0:
            temp = str(int(b[j]) * int(a[i]) + remainder)
            if len(temp) > 1:
                remainder = int(temp[0])
                agg = temp[1] + agg
            else:
                remainder = 0
                agg = temp[0] + agg
            j -= 1
        print agg
        product += int(agg)
        i -= 1

    product = str(product)
    return int(product[len(product) - digits:len(product) + 1])

def nextPrime(n):
    if n % 2 == 0:
        n -= 1

    isPrime = False

    while not isPrime:
        isPrime = True
        n += 2
        sqrt = int(math.sqrt(n))

        for p in primes(n):
            if p <= sqrt:
                if n % p == 0:
                    isPrime = False
                    break
            else:
                break

    return n

def primeRangeList(lower, upper):
    plist = []
    current = lower
    if not isPrime(lower):
        current = nextPrime(current)

    while current <= upper:
        plist.append(current)
        current = nextPrime(current)

    return plist

def explode(n, mod):
    cur = 1
    count = 1
    while count < n:
        cur = (6 * cur ** 2 + 10 * cur + 3) % mod
        count += 1
    return cur


sum = 0
for p in primeRangeList(10 ** 9, 10 ** 9 + 10 ** 3):
    print p
    sum += explode(10 ** 15,p)

print sum
