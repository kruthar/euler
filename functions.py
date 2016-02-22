__author__ = 'kruthar'

from decimal import *
import generators
import math
import decimal

# Get a list of multiples of a given base less then a given limit
def getMultiples(base, limit):
    current = base
    multiples = []

    while current < limit:
        multiples.append(current)
        current += base

    return multiples

# Merge given lists a and b with no duplicates, merged list shall be sorted
def mergeLists(a, b):
    append = []
    for item in a:
        if item not in b:
            append.append(item)

    b += append
    b.sort()

    return b

# Get the sum of a list of integers
def sumList(list):
    total = 0

    for num in list:
        total += num

    return total

# Get the product of a list of integers
def prodList(list):
    total = 1

    for num in list:
        total *= num

    return total

# Get the prime factorization of the given number (this includes duplicate factors)
def primeFactorization(num):
   factors = dict()
   current = num
   pgen = generators.primes()

   if num < 2:
       return dict()

   if isPrime(num):
       return {num: 1}

   while current > 1:
       prime = pgen.next()
       while current % prime != 0:
           prime = pgen.next()

       factors[prime] = 1
       current /= prime
       while current % prime == 0:
           factors[prime] += 1
           current /= prime

       if isPrime(current):
           factors[current] = 1
           current = 0

   return factors

primeFactorCache = dict()

# Flatten a prime factorization map to a list with repeated factors
def factMapToList(map):
    list = []
    for key, value in map.iteritems():
        for i in range(value):
            list.append(key)
    return list

# Get a list of lists of factors that multiple up to n
def getMultiplicationGroups(n):
    return gmgHelper(factMapToList(primeFactorization(n)))

def gmgHelper(list):
    if len(list) == 0:
        return [[]]
    groups = []
    for g in gmgHelper(list[1:]):
        added = sorted(g[:] + [list[0]])
        if added not in groups:
            groups.append(added)
        for i, item in enumerate(g):
            mult = g[:]
            mult[i] = mult[i] * list[0]
            mult.sort()
            if mult not in groups:
                groups.append(mult)
    return groups
    '''
    for i in range(1, len(list) + 1):
        temp = list[i:]
        for sub in gmgHelper(temp):
            g = sorted([prodList(list[0:i])] + sub)
            if g not in groups:
                groups.append(g)
    return groups
    '''

# Get the prime factors of a given number (does not include duplicates)
def primeFactors(num):
    if primeFactorCache.has_key(num):
        return primeFactorCache[num]

    primes = primeFactorization(num).keys()
    primeFactorCache[num] = primes

    for key in primes:
        for i in range(1, 10):
            primeFactorCache[num * key ** i] = primes

    return primes

# Get the smallest multiple given a list of numbers
def smallestMultiple(nums):
    factors = dict()

    for num in nums:
        factorization = primeFactorization(num)
        for key, value in factorization.iteritems():

            if factors.has_key(key) and factors[key] > value:
                # We already contain the correct number or more of this factor
                pass
            else:
                factors[key] = value
    return factors

# Check if given string is a palindrome
def isPalindrome(string):
    x = 0
    y = len(string) - 1

    while x <= y:
        if string[x] != string[y]:
            return False
        x += 1
        y -= 1

    return True

divisorCache = dict()

def getDivisors(num):
    if divisorCache.has_key(num):
        return divisorCache[num]

    divisors = []
    sqrt = math.ceil(math.sqrt(num))
    current = 1

    while current <= sqrt:
        if num % current == 0:
            quotient = num / current
            if quotient not in divisors:
                divisors.append(quotient)
            if current not in divisors:
                divisors.append(current)
        current += 1

    divisors.sort()
    divisorCache[num] = divisors
    return divisors

def getProperDivisors(num):
    result = getDivisors(num)
    result.remove(num)
    return result

def getReciprocalCycle(denom):
    prec = 100
    getcontext().prec = prec
    decimal = str(Decimal(1) / Decimal(denom)).split('.')[1]
    reciprocal = dict()

    if len(decimal) < prec:
        reciprocal['base'] = decimal
        reciprocal['cycle'] = ''
        return reciprocal

    for i in range(0, len(decimal)):
        for j in range(i + 1, len(decimal)):
            if decimal[i] == decimal[j]:
                like = True
                k = j
                reps = 0
                while reps == 0:
                    while k + (j - i) < prec:
                        reps += 1
                        if decimal[i:j] != decimal[k:k + j - i]:
                            like = False
                            break
                        k += j - i
                    if reps == 0:
                        prec *= 2
                        getcontext().prec = prec
                        decimal = str(Decimal(1) / Decimal(denom)).split('.')[1]

                if like and reps > 0:
                    reciprocal['base'] = decimal[0:i]
                    reciprocal['cycle'] = decimal[i:j]
                    return reciprocal

    reciprocal['base'] = decimal
    reciprocal['cycle'] = ''
    return reciprocal

def isAbundant(num):
    return sumList(getDivisors(num)) - num > num

primeCache = dict()

def isPrime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if primeCache.has_key(num):
        return primeCache[num]

    result = True

    for p in generators.primes(math.sqrt(num) + 1):
        if num % p == 0:
            result = False
            break

    primeCache[num] = result

    return result

def isCircularPrime(num):
    circular = True
    s = str(num)
    for a in range(len(str(num))):
        if not isPrime(int(s[a:] + s[0:a])):
            circular = False
    return circular

binaries = dict()

def getBinary(num):
    if binaries.has_key(num):
        return binaries[num]

    place = 1
    current = num
    binary = ''

    while place < num:
        place *= 2

    while place > 0:
        if place <= current:
            binary += '1'
            current -= place
        elif len(binary) > 0:
            binary += '0'
        place /= 2

    binaries[num] = binary

    return binary

def isTruncatablePrime(prime):
    truncatable = True
    sprime = str(prime)

    if len(sprime) < 2:
        return False

    for a in range(1, len(sprime)):
        if not isPrime(int(sprime[0:-a])):
            truncatable = False
            break
        if not isPrime(int(sprime[a:])):
            truncatable = False
            break

    return truncatable

def isPandigital(string, zero = False):
    start = 1
    count = 0

    if zero:
        start = 0

    for a in range(start, len(string) + (1 * start)):
        count += 1
        if str(a) not in string:
            return False

    return True and count + start == 10

def getWordScore(word):
    score = 0
    for letter in word:
        score += ord(letter) - 64
    return score

def isPermutation(num, perm):
    return ''.join(sorted(num)) == ''.join(sorted(perm))

def getStarPerms(string, start = 1):
    if start >= len(string):
        return [string]

    perms = []
    perms += getStarPerms(string, start + 1)
    perms += getStarPerms(string[0:start] + '*' + string[start + 1:], start + 1)

    return perms

def getContinuedFraction(num, expansions, start = {}):
    # find the sqrt of num to get the base integer part and the remaining fraction
    getcontext().prec = 1000
    sqrt = Decimal(num).sqrt()
    count = 0

    if start.has_key('base'):
        result = start
        count = len(start['list'])
        fraction = start['fraction']
    else:
        result = {'base': int(math.floor(sqrt)), 'list': []}
        fraction = sqrt - result['base']

    # Perform the specified number of expansions
    while count < expansions:
        # invert remaining fraction
        temp = Decimal(1) / fraction

        # retrieve the integer part of the expansion
        intpart = int(math.floor(temp))

        # retrieve the remaining fraction part of the expansion
        fraction = temp - intpart

        # save the integer part
        result['list'].append(intpart)
        result['fraction'] = fraction
        count += 1

    return result

def simplifyContinuedFraction(cf, start = 0):
    numer = 1
    denom = cf['list'][-1]
    count = len(cf['list'])
    expansions = dict()

    for a in cf['list'][::-1][0:]:
        for exp in expansions.iterkeys():
            tmp = expansions[exp]['denom'] + expansions[exp]['numer'] * a
            expansions[exp]['denom'] = expansions[exp]['numer']
            expansions[exp]['numer'] = tmp

        expansions[count] = {'numer': a, 'denom': 1}
        count -= 1

    for exp in expansions.iterkeys():
        tmp = expansions[exp]['denom'] + expansions[exp]['numer'] * cf['base']
        expansions[exp]['denom'] = expansions[exp]['numer']
        expansions[exp]['numer'] = tmp

    return expansions

decimals = dict()

def getDecimal(binary):
    if decimals.has_key(binary):
        return decimals[binary]

    result = 0
    current = 1

    for digit in binary[::-1]:
        if digit == '1':
            result += current
        current *= 2

    decimals[binary] = result

    return result

xors = dict()

def xor(a, b):
    ax = a[:]
    bx = b[:]
    key = min(ax, bx) + max(ax, bx)
    if xors.has_key(key):
        return xors[key]
    result = ''

    if len(ax) < len(bx):
        for i in range(len(bx) - len(ax)):
            ax = '0' + ax
    if len(bx) < len(ax):
        for i in range(len(ax) - len(bx)):
            bx = '0' + bx
    for i in range(len(ax)):
        if ''.join(sorted(ax[i] + bx[i])) == '01':
            result += '1'
        else:
            result += '0'

    xors[key] = result

    return result

def totient(num):
    if num == 1:
        return 1
    product = num
    for factor in primeFactors(num):
        product *= (1 - 1.0 / factor)
    return int(product)

def hcf(a, b):
    adiv = getDivisors(a)
    max = 0

    for ad in adiv:
        if b % ad == 0 and ad > max:
            max = ad

    return max

def relativelyPrime(a, b):
    pgen = generators.primes()
    current = pgen.next()
    while current <= a:
        if a % current == 0 and b % current == 0:
            return False
        current = pgen.next()

    return True

def manualSquare(n, digits):
    string = str(n)
    prefix = ''
    index = 0
    result = ''
    current = ''
    integer = len(str(int(math.floor(math.sqrt(n)))))

    if len(str(n)) % 2 == 1:
        string = '0' + str(n)
    else:
        string = str(n)

    while len(result) < integer + digits:
        if index + 2 <= len(string):
            current += string[index:index + 2]
        else:
            current += '00'
        square = 1

        if result != '':
            prefix = str(2 * int(result))
        else:
            prefix = ''

        while int(prefix + str(square)) * square <= int(current):
            square += 1

        square -= 1

        result += str(square)
        current = str(int(current) - int(prefix + str(square)) * square)

        index += 2

    return result[0:integer] + '.' + result[integer:integer + digits]

def gcd(list):
    divisors = getDivisors(list[0])
    greatest = 1
    for n in list[1:]:
        ndivs = getDivisors(n)
        newlist = []
        for div in ndivs:
            if div in divisors:
                newlist.append(div)
        divisors = newlist[:]

    for com in divisors:
        if com > greatest:
            greatest = com

    return greatest

def isSquare(num):
    s = int(math.sqrt(num))
    return s * s == num